<div align="center">
  <a href="https://nb.novelai.dev"><img src="imgs/head.jpg" width="180" height="180" alt="NoneBot-plugin-novelai" style="border-radius:100%; overflow:hidden;"></a>
  <br>
</div>

<div align="center">

# Nonebot-plugin-novelai

_✨ 中文输入、对接 webui、以及你能想到的大部分功能 ✨_

[讨论群](https://jq.qq.com/?_wv=1027&k=pT3Mn4jG)|[说明书](https://nb.novelai.dev)|[整合包]()|[ENGLISH](./README_EN.md)

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/sena-nana/nonebot-plugin-novelai" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-novelai">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-novelai" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 功能介绍

- AI 绘画
  - 支持 CD 限速和绘画队列
  - 支持高级请求语法
  - 内置翻译 Api，自动翻译中文
  - 内置屏蔽词，可设置全局词条和排除词条
  - 返回消息支持简洁模式和详细模式
  - 模拟官方的点数管理模式，并能够按用户限制总额和每日使用量
  - 支持多后端负载均衡(Todo)
  - 支持自定义回复格式(Todo)
- 管理
  - 支持群黑白名单
  - 提供了管理指令用于运行时修改部分设置
  - Web 管理界面(Todo)
- 支持后端
  - novelai 官网
  - naifu
  - stable diffusion webui(本地，远程 or colab)
  - 另一个 novelai 插件(Todo)
  - 由第三方扩展的后端
- 扩展功能
  - 查询图片 TAG
  - 由第三方实现的扩展
- 自我管理
  - 版本检查和更新提醒，支持插件热更新和自动重启
  - 内置简易权限管理，被封退群，加群管理(Todo)

## 💿 安装

<details>
<summary>使用 nb-cli 安装 (推荐)</summary>

1. 在 nonebot2 项目的根目录下打开终端
2. 如果你是 Windows 用户，输入`./.venv/Scripts/activate`并回车，如果你是 Linux 用户，输入`source ./.venv/bin/activate`并回车。你应该能够看到终端在新的一行激活了虚拟环境。如果你使用旧版 nb-cli 创建的项目不存在.venv 文件夹，则跳过此步骤

3. 最后输入以下指令即可安装

```
nb plugin install nonebot-plugin-novelai
```

</details>
<details>
<summary>使用包管理器安装</summary>

1. 在 nonebot2 项目的根目录下, 打开终端
2. 如果你是 Windows 用户，输入`./.venv/Scripts/activate`并回车，如果你是 Linux 用户，输入`source ./.venv/bin/activate`并回车。你应该能够看到终端在新的一行激活了虚拟环境。如果你使用旧版 nb-cli 创建的项目不存在.venv 文件夹，则跳过此步骤
3. 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-novelai

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-novelai

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-novelai

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-novelai

</details>

4. 打开 nonebot2 项目的 `pyproject.toml` 文档, 在其中名为 **plugins** 的列表中，加入"nonebot-plugin-novelai"

</details>
<details>
<summary>下载源码安装 (不推荐)</summary>

> 除非你对自己解决问题的能力有信心，并且有着修改插件的需求，否则你不应该选择这种方法。这种方法无法通过以上两种方法更新版本，并会与插件内置的更新功能冲突

1. (nb-cli 版本 1.0 以上) 确保你在创建项目时选择的是开发者版项目结构，否则插件目录中不存在能够放置插件的文件夹。
2. 在 nonebot2 项目的根目录下打开命令行
3. 如果你是 Windows 用户，输入`./.venv/Scripts/activate`并回车，如果你是 Linux 用户，输入`source ./.venv/bin/activate`并回车。你应该能够看到终端在新的一行激活了虚拟环境。如果你使用旧版 nb-cli 创建的项目不存在.venv 文件夹，则跳过此步骤
4. 在 Github 中下载源代码
   1. [稳定版本](https://github.com/sena-nana/nonebot-plugin-novelai/releases/download/v0.6.0/nonebot_plugin_novelai.zip)
   2. [测试版本](https://github.com/sena-nana/nonebot-plugin-novelai/archive/refs/heads/main.zip)
5. 将上一步下载的 zip 文件打开，将**requirements.txt**复制至 bot 项目根目录备用，将**nonebot_plugin_novelai**文件夹解压至 bot 目录的 src/plugins 文件夹中
6. 在终端中运行下面的指令，如果你使用pip以外的包管理器，请使用对应的指令

```
pip install -r requirements.txt
```

7. 现在你可以删除**requirements.txt**文件了

</details>
## ⚙️ 配置

请前往说明书查看[全局配置](https://nb.novelai.dev/main/config.html)一节

## 🎉 使用

请前往说明书查看[使用](https://nb.novelai.dev/main/aidraw.html)一节

## 🌸 致谢

感谢[Novelai Bot](https://bot.novelai.dev/)提供的子域名，如果你更了解 Koishi 框架或是 Node.js，可以使用这个项目

感谢以下开发者对该项目做出的贡献：

<a href="https://github.com/sena-nana/nonebot-plugin-novelai/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sena-nana/nonebot-plugin-novelai" />
</a>
