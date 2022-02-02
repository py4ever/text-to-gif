#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/2 4:27 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : aaa.py
# @Project : text-to-gif


import emoji


def text_has_emoji(text: str):
    return emoji.emoji_count(text) > 0


def lines_has_emoji(lines: list):
    for text in lines:
        if text_has_emoji(text):
            return True
    return False


if __name__ == '__main__':
    print(emoji.emojize(u'I \u2764 emoji'))
    print(text_has_emoji(u'I \u2764 emoji'))
    print(text_has_emoji(emoji.demojize('I ❤️️ emoji')))
    print("emoji:", emoji.demojize('㊗️ emoji'))
    print("count:", emoji.emoji_count('㊗️ emoji'))
    print("lines_has_emoji:", lines_has_emoji(['㊗️ emoji']))
    print("lines_has_emoji:", lines_has_emoji(['㊗emoji']))
    print("lines_has_emoji:", lines_has_emoji(['no emoji']))
