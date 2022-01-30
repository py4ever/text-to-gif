text-to-gif
=========

AKA t2g or text-to-gif-cli on pypi

Well, I didn't find a python lib to process the text as gif.

So I developed this.

It can help me to create gif with code execution result if I don't have change to upload the live-running video.

t2g(text-to-gif) 支持开发者把文本转化为gif进行动态播放。

学委写了很多文章都是贴静态图的，今年改进一下，发现市场没有这样的。所以用python写了一个小工具。

支持把 文本/代码 转化为gif 动态展示。

Package hosted on [`pypi`_] and powered by [`pypi-seed`_]


Installation / 安装
--------------------------

::

    pip install text-to-gif




Quick start / 使用
--------------------------

比如下面的命令可以把 xuewei_pypi_blog.txt 文件生成一个5帧的 gif 图片

::

    t2g -p /Users/mac/PycharmProjects/hello/xuewei_pypi_blog.txt -d ./blog.gif -f 5



More Info
--------------------------

Author levin

.. _`pypi`: https://pypi.org/
.. _`pypi-seed`: https://pypi.org/project/pypi-seed/

