# text-to-gif

AKA t2g or text-to-gif-cli on pypi

Well, I didn't find a python lib to process the text as gif.

So I developed this.

It can help me to create gif from pure text input.

t2g(text-to-gif) 支持开发者把文本转化为gif进行动态播放。

学委写了很多文章都是贴静态图的，后来准备改成gif动图。

发现市场没有这样的。所以用python写了一个小工具。

**它支持把 文本/代码 转化为gif 动态展示。**

If there is a 'input.txt' on current dir

We can just run 't2g'.

And it will generate text2gif.gif file on current dir with default options

Powered by [pypi-seed](https://pypi.org/project/pypi-seed/)

# Quickstart

Usage doc generation:

[![usage_doc.gif](https://raw.githubusercontent.com/py4ever/text-to-gif/master/usage_doc.gif)](https://github.com/py4ever/text-to-gif/tree/master/usage_doc)

So any github user can use this tool to generate usage_doc.gif or specify your quick start doc as gif

Run with emoji in text file:

[![demo_emoji.gif](https://raw.githubusercontent.com/py4ever/text-to-gif/master/demo_emoji.gif)](https://github.com/py4ever/text-to-gif/tree/master/demo_emoji)

In case the above gif not rendering so well:

![](usage_doc.gif)
# Installation / 安装

Get t2g by pip (通过PIP工具来安装text-to-gif)

```bash
pip install text-to-gif
```

Print the usage

```bash
t2g -h
```

# Use text-to-gif as CLI / 命令行使用

We can call the cli 't2g' or 'text-to-gif' or 'ttg'： \
调用下面两个命令行即可。

```bash
t2g -p /Users/mac/PycharmProjects/hello/xuewei_pypi_blog.txt -d ./blog.gif -f 5
```

```bash
ttg -p /Users/mac/PycharmProjects/hello/xuewei_pypi_blog.txt -d ./blog.gif -f 5
```

```bash
text2gif -p /Users/mac/PycharmProjects/hello/xuewei_pypi_blog.txt -d ./blog.gif -f 5
```

The above command will generate below gif:

[![blog.gif](https://raw.githubusercontent.com/py4ever/text-to-gif/master/blog.gif)](https://github.com/py4ever/text-to-gif/tree/master/blog)

# More Info

Author 雷学委

## The features

- support text file into gif file in multi frames within default/specific duration

- support text file with emoji

For this support, t2g uses [pilmoji](https://pypi.org/project/pilmoji) to handle emoji

- support user to provider a folder as input, t2g will collect list  of  text file(*.txt) first

If there is not text file, it will try to collect list of logs (*.log) file and render them as a n frame gif(n=the number of match files)

- run 't2g-opt'  to check out the t2g environment variables to enable your own customization

t2g-opt will print the env var, and you can set the default value.

