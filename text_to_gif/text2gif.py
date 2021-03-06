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
from urllib.error import URLError

from PIL import Image, ImageDraw, ImageFont
from pilmoji import Pilmoji

from text_to_gif.emoji_check import text_has_emoji, lines_has_emoji
from text_to_gif.env_options import get_font, do_ssl_check, get_font_size
from text_to_gif.gif_creator import create_gif
from text_to_gif.image_file_filter import filter_and_sort

TEXT_COLOR_WHITE = (255, 255, 255)


def font_support_chinese():
    try:
        user_font = get_font()
        if user_font is None:
            return ImageFont.load_default()
        font_size = get_font_size()
        font = ImageFont.truetype(user_font, font_size)
        return font
    except:
        font: ImageFont = ImageFont.load_default()
        return font


def draw_normal_text(font, frame_size, page_index, img, img_line, lines):
    page_data = lines[img_line * page_index:img_line * (page_index + 1)] if page_index != frame_size - 1 else lines[
                                                                                                              img_line * page_index:]
    draw_all_normal_text(font, page_index, img, page_data)


def draw_all_normal_text(font, page_index, img, lines):
    diag = ImageDraw.Draw(img)
    location = (10, 10)
    diag.text(location, '#Powered by text-to-gif - p' + str(page_index + 1), fill=TEXT_COLOR_WHITE, font=font)
    page_data = lines
    counter = 1
    for line in page_data:
        counter += 1
        location = (10, 20 * counter)
        diag.text(location, line, fill=TEXT_COLOR_WHITE, font=font)


# text_files, frame_size, max_line_text_len,max_page_height, gif_dest, verbose, duration
def transform_dir_to_gif(text_files, frame_size: int,
                         max_line_text_len: int,
                         max_page_height: int,
                         gif_dest: str, verbose: bool,
                         duration: float = 0.6):
    height = int(max_page_height * 25)
    height = 300 if height < 300 else height
    with TemporaryDirectory(prefix=".text_capture", suffix=".png",
                            dir=os.getcwd()) as tmpdir:
        logging.debug("tmp dir:%s", tmpdir)
        for i in range(frame_size):
            final_img_path = os.path.join(tmpdir, "pic" + str(i)) + ".png"
            width = int(max_line_text_len * 10)
            img_size = (width, height)
            font = font_support_chinese()
            img = Image.new('RGB', img_size)
            current_file = text_files[i]
            with open(current_file, 'r') as f:
                lines = f.readlines()
                if lines_has_emoji(lines):
                    try:
                        draw_all_text_with_emoji_support(font, i, img, lines)
                    except URLError as err:
                        logging.warning("probably network issue, err:%s", err)
                        draw_all_normal_text(font, i, img, lines)
                else:
                    draw_all_normal_text(font, i, img, lines)
            logging.debug("will save img : %s", final_img_path)
            img.save(final_img_path)
        image_list = filter_and_sort(tmpdir)
        gif_file_path = os.path.join(os.getcwd(), gif_dest)
        create_gif(image_list, gif_file_path, duration)
        # print("verbose:%s" % verbose)
        if verbose:
            print("gif created at %s" % gif_file_path)


def transform_text_to_gif(lines, frame_size: int,
                          max_line_text_len: int,
                          gif_dest: str, verbose: bool,
                          duration: float = 0.6):
    total_line = len(lines)
    if verbose and lines_has_emoji(lines):
        logging.info("input text contains emoji")
    img_line = math.floor(total_line / frame_size)
    if total_line % frame_size != 0:
        img_line += 1
    with TemporaryDirectory(prefix=".text_capture", suffix=".png",
                            dir=os.getcwd()) as tmpdir:
        logging.debug("tmp dir:%s", tmpdir)
        for i in range(frame_size):
            final_img_path = os.path.join(tmpdir, "pic" + str(i)) + ".png"
            height = int(total_line / frame_size * 25)
            height = 300 if height < 300 else height
            width = int(max_line_text_len * 10)
            img_size = (width, height)
            font = font_support_chinese()
            img = Image.new('RGB', img_size)
            if lines_has_emoji(lines):
                try:
                    draw_text_with_emoji_support(font, frame_size, i, img, img_line, lines)
                except URLError as err:
                    logging.warning("probably network issue, err:%s", err)
                    draw_normal_text(font, frame_size, i, img, img_line, lines)
            else:
                draw_normal_text(font, frame_size, i, img, img_line, lines)
            logging.debug("will save img : %s", final_img_path)
            img.save(final_img_path)
        image_list = filter_and_sort(tmpdir)
        gif_file_path = os.path.join(os.getcwd(), gif_dest)
        create_gif(image_list, gif_file_path, duration)
        # print("verbose:%s" % verbose)
        if verbose:
            print("gif created at %s" % gif_file_path)


def draw_text_with_emoji_support(font, frame_size, page_index, img, img_line, lines):
    page_data = lines[img_line * page_index:img_line * (page_index + 1)] if page_index != frame_size - 1 else lines[
                                                                                                              img_line * page_index:]
    draw_all_text_with_emoji_support(font, page_index, img, page_data)


def draw_all_text_with_emoji_support(font, page_index, img, lines):
    if not do_ssl_check():
        # urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
    with Pilmoji(img) as pilmoji:
        location = (10, 10)
        counter = 1
        pilmoji.text(location, '#Powered by text-to-gif - p' + str(page_index + 1), fill=TEXT_COLOR_WHITE, font=font)
        page_data = lines
        for line in page_data:
            counter += 1
            location = (10, 20 * counter)
            pilmoji.text(location, line, fill=TEXT_COLOR_WHITE, font=font)


def text2gif(long_text_path: str, frame_size: int = 3,
             gif_dest: str = "text2gif.gif",
             verbose: bool = False,
             duration: float = 0.6):
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
        transform_text_to_gif(lines, frame_size, max_line_text_len, gif_dest, verbose, duration)


def textfolder2gif(text_files: list, frame_size: int = 3,
                   gif_dest: str = "text2gif.gif",
                   verbose: bool = False,
                   duration: float = 0.6):
    if verbose:
        print("text files:%s, frame:%s, destination:%s" % (text_files, frame_size, gif_dest))
    max_line_text_len = 80
    max_page_height = 0
    for text_file in text_files:
        with open(text_file, 'r') as f:
            lines = f.readlines()
            if max_page_height < len(lines):
                max_page_height = len(lines)
            for line in lines:
                if max_line_text_len < len(line):
                    max_line_text_len = len(line)
    if max_line_text_len > 160:
        max_line_text_len = 160
    transform_dir_to_gif(text_files, frame_size, max_line_text_len, max_page_height, gif_dest, verbose, duration)


if __name__ == "__main__":
    text_path = "/Users/mac/PycharmProjects/cv2sample/images/input/leixuewei_sample.log"
    text_path = "/Users/mac/python/text-to-gif/demo_emoji.txt"
    text2gif(long_text_path=text_path, verbose=True, duration=2)
    # text2gif(long_text_path=text_path, verbose=False, duration=1.5)
