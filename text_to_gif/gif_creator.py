#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/30 8:59 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: OpenSource
# @File : gif_creator.py
# @Project : text-to-gif


import imageio


def create_gif(image_list, gif_file_path, duration=0.33):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_file_path, frames, 'GIF', duration=duration)
