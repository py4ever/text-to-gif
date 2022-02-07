#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/4 4:16 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : env_options.py
# @Project : text-to-gif

import os

T2G_DEFAULT_FONT = 'T2G_DEFAULT_FONT'
T2G_DEFAULT_FONT_SIZE = 'T2G_DEFAULT_FONT_SIZE'
T2G_DO_SSL_CHECK = 'T2G_DO_SSL_CHECK'
T2G_SKIP_USAGE_DOC = 'T2G_SKIP_USAGE_DOC'


def print_all_opts_doc():
    doc = dict()
    doc[T2G_DEFAULT_FONT] = """t2g default font for user to specify to avoid any text rendering issue.
                            sample value like 'Hiragino Sans GB.ttc'(system loaded font file name)
                            
                            please find font(*.ttf/*.ttc) on your system font directory.
                            A filename or file-like object containing a TrueType font.
                             If the file is not found in this filename, the loader may also
                             search in other directories, such as the :file:`fonts/`
                             directory on Windows or :file:`/Library/Fonts/`,
                             :file:`/System/Library/Fonts/` and :file:`~/Library/Fonts/` on
                             macOS.
                            """
    doc[T2G_DEFAULT_FONT_SIZE] = """t2g default font size when user has specified default font to avoid any text rendering issue.
                            sample value like 14 or 12 (or any number)
                            """
    doc[
        T2G_DO_SSL_CHECK] = """When rendering emoji, t2g will ask emoji website through a https connection.
        by default ssl check will be disabled. You can turn it on
        
        """
    doc[
        T2G_SKIP_USAGE_DOC] = """The t2g program will lookup the input.txt file first.
        If not exist and this flag is not set or 'False', it will try to load user doc txt file by default"""
    print("option documentation")
    for k, v in doc.items():
        print("t2g env key %s = %s" % (k, v))


def skip_user_doc_load():
    skip_usage_doc = get_value(T2G_SKIP_USAGE_DOC, False)
    try:
        skip_usage_doc = True if skip_usage_doc == 'True' or skip_usage_doc == 'TRUE' or skip_usage_doc == '1' else False
    except:
        skip_usage_doc = False
    return skip_usage_doc


def do_ssl_check():
    return get_value(T2G_DO_SSL_CHECK, False)


def get_font():
    return get_value(T2G_DEFAULT_FONT, "Hiragino Sans GB.ttc")  # this can show chinese text


def get_font_size():
    return get_value(T2G_DEFAULT_FONT_SIZE, 14)


def get_value(key, default_value):
    val = os.environ[key] if key in os.environ else default_value
    return val


if __name__ == "__main__":
    print_all_opts_doc()
