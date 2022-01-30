#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/30 5:29 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : text-to-gif.py
# @Project : text-to-gif
import locale
import math
import os
import time
import logging
from tempfile import NamedTemporaryFile, TemporaryDirectory

from PIL import Image, ImageDraw, ImageFont

from text_to_gif.gif_creator import create_gif
from text_to_gif.image_file_filter import filter_and_sort

TEXT_COLOR_WHITE = (255, 255, 255)


def font_support_chinese():
    try:
        font_name = "Hiragino Sans GB.ttc"  # this can show chinese text
        fontsize = 14
        font = ImageFont.truetype(font_name, fontsize)
        return font
    except:
        return ImageFont.load_default()


def transform_text_to_gif(lines, frame_size: int,
                          max_line_text_len: int,
                          gif_dest: str, verbose: bool,
                          duration: float = 0.6):
    total_line = len(lines)
    img_line = math.floor(total_line / frame_size)
    if total_line % frame_size != 0:
        img_line += 1
    with TemporaryDirectory(prefix=".text_capture", suffix=".png",
                            dir=os.getcwd()) as tmpdir:
        logging.debug("tmp dir:%s", tmpdir)
        for i in range(frame_size):
            final_img_path = os.path.join(tmpdir, "pic" + str(i)) + ".png"
            counter = 1
            height = int(total_line / frame_size * 25)
            height = 300 if height < 300 else height
            width = int(max_line_text_len * 10)
            img_size = (width, height)
            img = Image.new('RGB', img_size)
            diag = ImageDraw.Draw(img)
            location = (10, 10)
            font = font_support_chinese()
            diag.text(location, '#Powered by text-to-gif - p' + str(i + 1), fill=TEXT_COLOR_WHITE, font=font)
            page_data = lines[img_line * i:img_line * (i + 1)] if i != frame_size - 1 else lines[img_line * i:]
            for line in page_data:
                counter += 1
                location = (10, 20 * counter)
                diag.text(location, line, fill=TEXT_COLOR_WHITE, font=font)
            logging.debug("will save img : %s", final_img_path)
            img.save(final_img_path)
        image_list = filter_and_sort(tmpdir)
        gif_file_path = os.path.join(os.getcwd(), gif_dest)
        create_gif(image_list, gif_file_path, duration)
        #print("verbose:%s" % verbose)
        if verbose:
            print("gif created at %s" % gif_file_path)


def text2gif(long_text_path: str, frame_size: int = 3, gif_dest: str = "text2gif.gif", verbose: bool = False):
    if verbose:
        print("text file:%s, frame:%s, destination:%s" % (long_text_path, frame_size, gif_dest))
    with open(long_text_path, 'r') as f:
        lines = f.readlines()
        max_line_text_len = 80
        for line in lines:
            if max_line_text_len < len(line):
                max_line_text_len = len(line)
        if max_line_text_len > 160:
            max_line_text_len = 160
        transform_text_to_gif(lines, frame_size, max_line_text_len, gif_dest, verbose)


if __name__ == "__main__":
    text_path = "/Users/mac/PycharmProjects/cv2sample/images/input/leixuewei_sample.log"
    text2gif(long_text_path=text_path, verbose=True)
