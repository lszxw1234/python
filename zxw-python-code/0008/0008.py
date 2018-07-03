# -*- coding: utf-8 -*-
"""
第 0008 题：一个HTML文件，找出里面的正文。
"""

import requests, re, lxml
from bs4 import BeautifulSoup

url = 'http://www.cnblogs.com/piperck/p/5840443.html'

data = requests.get(url)
print('---------------------------------------------------------------')
soup = BeautifulSoup(data.text,'lxml')
print(soup.body.text)