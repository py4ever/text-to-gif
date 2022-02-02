#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @PypiSeedTag: Main
# @File : main.py
# @Project : text-to-gif


"""
generated by PypiSeed(PPC) - Main Program
"""
import argparse
import os

from text_to_gif.text2gif import text2gif

THE_DEFAULT_INPUTS = ["input.txt", "usage_doc.txt"]


def main():
    parser = argparse.ArgumentParser(
        description="Please provide params to call t2g(text-to-gif) or just run it to generate usage_doc.gif")
    parser.add_argument('--input', '-i', default="input.txt",
                        help="tell t2g where is the (long)text input file path, default is 'input.txt'(load first) or 'usage_doc.txt' ")
    parser.add_argument('--output', '-o', default="usage_doc.gif",
                        help="tell t2g where to store the output gif, default is 'usage_doc.gif'")
    parser.add_argument('--duration', '-d', default=0.66, type=float,
                        help="the duration of output gif, 0.66 as default")
    parser.add_argument('--frame', '-f', default=3, type=int,
                        help="tell t2g how many frame to structure the long text into multi-frame in output gif, 3 as default")
    parser.add_argument('--verbose', '-v', action='store_const', const=True, help="show more verbose info(optional)")
    args = parser.parse_args()
    long_text_path = args.input
    usage_doc_loaded = False
    verbose = args.verbose
    if verbose is None:
        verbose = False
    if long_text_path and long_text_path not in THE_DEFAULT_INPUTS:
        # so current user has specific the input file and not in any default input
        if not os.path.exists(long_text_path):
            raise ValueError("The input file does not exist, path:" + long_text_path)
    elif not os.path.exists(long_text_path):
        skip_usage_doc = os.environ['T2G_SKIP_USAGE_DOC'] if 'T2G_SKIP_USAGE_DOC' in os.environ else False
        try:
            skip_usage_doc = True if skip_usage_doc == 'True' or skip_usage_doc == 'TRUE' or skip_usage_doc == '1' else False
        except:
            skip_usage_doc = False
        if skip_usage_doc:
            raise ValueError("The input file does not exist, path:" + long_text_path)
        else:
            usage_doc_path = "usage_doc.txt"
            if os.path.exists(usage_doc_path):
                usage_doc_loaded = True
                long_text_path = usage_doc_path
            else:
                raise ValueError("The input file does not exist, path:" + long_text_path)
    frame_size = args.frame
    if frame_size <= 0:
        print("Invalid frame size(should be at least 1 or more.")
        return
    duration = args.duration
    if duration <= 0:
        print("Invalid duration(must > 0)")
        return
    output = args.output
    if verbose:
        print("input:%s, output:%s with frame:%s duration %s" %
              (long_text_path, output, frame_size, duration))
    text2gif(long_text_path, frame_size, output, verbose, duration)


if __name__ == '__main__':
    main()
