#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。


class Input(object):
    def __init__(self):
        self.filter_words = list()
        self.in_strings = ''
        self.out_strings = ''
        self.load_filter_words()


    def load_filter_words(self, filename='filter_words.txt'):
        with open(filename, 'r', encoding='utf8') as file:
            for line in file:
                self.filter_words.append(line.strip())


    def user_input(self):
        self.in_strings = input('>')

    def std_output(self):
        self.filter_word()
        print(self.out_strings)

    def filter_word(self):
        self.out_strings = self.in_strings
        for word in self.filter_words:
            if self.out_strings.find(word) != -1:
                self.out_strings = self.out_strings.replace(word, '*'*len(word))







i = Input()
i.user_input()
i.std_output()