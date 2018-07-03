# -*- coding: utf-8 -*-
"""
第 0009 题：一个HTML文件，找出里面的链接。
"""

import requests, re, lxml
from bs4 import BeautifulSoup

url = 'http://www.cnblogs.com/piperck/p/5840443.html'

data = requests.get(url)

aurls = re.findall(r'<a.*href=\"(.*?)\".*</a>',data.text)
print(aurls)
urls = re.findall(r'<a.*href=\"(.*?)\".*</a>',data.text)
print(urls)