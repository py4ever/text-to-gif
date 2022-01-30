#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/23 4:14 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: OpenSource
# @File : gif_creator.py
# @Project : text-to-gif

import os


def filter_and_sort(dir, pattern=None):
    data = filter_by_pattern(dir, pattern)
    data.sort()
    return data


def filter_by_pattern(dir, pattern=None):
    files = os.listdir(dir)
    subfiles = []
    for f in files:
        fullpath = os.path.join(dir, f)
        if os.path.isdir(fullpath):
            subfiles.extend(filter(fullpath, pattern))
        else:
            if pattern is None or pattern in f:
                subfiles.append(fullpath)
    return subfiles


if __name__ == "__main__":
    # files = filter("../images/animation/runcode")
    files = filter_by_pattern("../images/animation/", "threading")
    print("files:", files)
