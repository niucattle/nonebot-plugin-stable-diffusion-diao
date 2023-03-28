from ..config import config, nickname
from ..utils.save import save_img
from ..utils import sendtosuperuser
from io import BytesIO
import base64
import aiohttp
import nonebot
import os
import urllib
import re
from PIL import Image
from nonebot.adapters.onebot.v11 import MessageSegment, Bot, GroupMessageEvent
from nonebot.log import logger
from ..config import config 

async def check_safe_method(fifo, img_bytes, message):
    bot = nonebot.get_bot()
    raw_message = f"\n{nickname}已经"
    # 判读是否进行图片审核
    if config.novelai_pic_audit == None:
        for i in img_bytes:
            await save_img(fifo, i)
            message += MessageSegment.image(i)
    else:
        nsfw_count = 0
        for i in img_bytes:
            try:
                label, h = await check_safe(i)
            except RuntimeError as e:
                logger.error(f"NSFWAPI调用失败，错误代码为{e.args}")
                label = "unknown"
            if label != "explicit":
                message += MessageSegment.image(i)
            else:
                message += f"太涩了,让我先看, 这张图涩度{h}"
                nsfw_count += 1
                if config.novelai_h_type == 1:
                    await bot.send_private_msg(user_id=fifo.user_id, 
                                                message=f"悄悄给你看哦{MessageSegment.image(i)}")
                elif config.novelai_h_type == 2:
                    message_data = await sendtosuperuser(f"让我看看谁又画色图了{MessageSegment.image(i)}")
                    message_id = message_data["message_id"]
                    message_all = await bot.get_msg(message_id=message_id)
                    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                    img_url = re.search(url_regex, message_all["message"])
                    await bot.send_group_msg(group_id=fifo.group_id, message=f"这是图片的url捏,{img_url}")
                else:
                    await sendtosuperuser(f"让我看看谁又画色图了{MessageSegment.image(i)}")
        if nsfw_count > 0:
            message += f"有{nsfw_count}张图片太涩了，" + raw_message + "帮你吃掉了"
        # else:
        #     message += MessageSegment.image(i)
    await save_img(fifo, i, label)
    return message


async def check_safe(img_bytes: BytesIO):
    if config.novelai_pic_audit == 2:
        try:
            import tensorflow as tf
        except:
            os.system("git lfs install && git clone https://huggingface.co/spaces/mayhug/rainchan-image-porn-detection && pip install tensorflow jinjia2")
            import tensorflow as tf
        from typing import IO
        from io import BytesIO
        SIZE = 224
        inter = tf.lite.Interpreter("rainchan-image-porn-detection/lite_model.tflite", num_threads=12)
        inter.allocate_tensors()
        in_tensor, *_ = inter.get_input_details()
        out_tensor, *_ = inter.get_output_details()


        async def process_data(content):
            img = tf.io.decode_jpeg(content, channels=3)
            img = tf.image.resize_with_pad(img, SIZE, SIZE, method="nearest")
            img = tf.image.resize(img, (SIZE, SIZE), method="nearest")
            img = img / 255
            return img


        async def main(file: IO[bytes]):
            data = process_data(file.read())
            data = tf.expand_dims(data, 0)
            inter.set_tensor(in_tensor["index"], data)
            inter.invoke()
            result, *_ = inter.get_tensor(out_tensor["index"])
            safe, questionable, explicit = map(float, result)
            possibilities = {"safe": safe, "questionable": questionable, "explicit": explicit}
            logger.debug("Predict result:", possibilities)
            return possibilities

        
        byte_img = base64.b64decode(img_bytes)
        # im = Image.open('1.jpg')
        # img_byte = BytesIO()
        # im.save(img_byte, format='JPEG') # format: PNG or JPEG
        # binary_content = img_byte.getvalue()
        file_obj = BytesIO(byte_img)
        possibilities = await main(file_obj)
        return possibilities

  
    async def get_file_content_as_base64(path, urlencoded=False):
        # 不知道为啥, 不用这个函数处理的话API会报错图片格式不正确, 试过不少方法了,还是不行(
        """
        获取文件base64编码
        :param path: 文件路径
        :param urlencoded: 是否对结果进行urlencoded 
        :return: base64编码信息
        """
        with open(path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content


    async def get_access_token():
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", 
                "client_id": config.novelai_pic_audit_api_key["API_KEY"], 
                "client_secret": config.novelai_pic_audit_api_key["SECRET_KEY"]}
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, params=params) as resp:
                json = await resp.json()
                return json["access_token"]


    with open("image.jpg", "wb") as f:
        f.write(img_bytes)
    base64_pic = await get_file_content_as_base64("image.jpg", True)
    payload = 'image=' + base64_pic
    token = await get_access_token()
    baidu_api = "https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined?access_token=" + token
    async with aiohttp.ClientSession() as session:
        async with session.post(baidu_api, data=payload) as resp:
            result = await resp.json()
            logger.debug(result)
            if result['conclusionType'] in [2, 3]:
                return "explicit", str(result['data'][0]['probability'])
    




