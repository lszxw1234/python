#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136x640)的大小。'


import os
import glob
from PIL import Image


def thumbnail_pic(path):
    name = os.path.join(path,'*.jpg')
    a = glob.glob(name)
    print(a)
    for x in a:
        im = Image.open(x)
        im.thumbnail((1136,640))
        print(im.format, im.size, im.mode, x)
        x = os.path.splitext(x)[0]
        print(x)
        im.save(x,'JPEG')
    print('Done!')



thumbnail_pic('C:\\Users\\zhango2\\Documents\\飞鸟\\飞鸟')