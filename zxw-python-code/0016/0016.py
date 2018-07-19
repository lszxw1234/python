#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中。'''



from openpyxl import Workbook
import json

def txt_to_xls(filename):
    file = open(filename,'r', encoding='utf-8')
    file_cintent = json.load(file, encoding='utf-8')
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'Citys'
    for i in range(1,len(file_cintent)+1):
        print(file_cintent)
        for i, list in enumerate(file_cintent,start=1):
            for j, num in enumerate(list,start=1):
                sheet.cell(row=i, column = j).value = num


    wb.save('numbers.xlsx')


txt_to_xls('numbers.txt')