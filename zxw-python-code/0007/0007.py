import os
import re

alllines = 0
codelines = 0
spacelines = 0
notelines = 0

def find_file(path):
    files = os.listdir(path)
    for file in files:
        fullname = os.path.join(path, file)
        if os.path.isdir(fullname):
            find_file(fullname)
        elif file.endswith('.py'):
            process_file(fullname)

#this is a test note
'''
didn't catch multi notes like these
'''
def process_file(filename):
    global alllines
    global codelines
    global spacelines
    global notelines
    with open(filename, 'r', encoding='utf8') as file:
        file_lines = 0
        file_spacelines = 0
        file_codelines = 0
        file_notelines = 0
        for line in file:
            _line = line.strip()
            file_lines += 1
            if not _line:
                file_spacelines += 1
            elif _line.startswith('#'):
                file_notelines += 1
            else:
                file_codelines += 1

        alllines += file_lines
        codelines += file_codelines
        spacelines += file_spacelines
        notelines += file_notelines
        print(filename, file_lines, file_codelines, file_spacelines, file_notelines)

find_file('C:\\Users\\zhango2\\PycharmProjects\\LearningPython\\zxw-python-code\\0007')
print('=' * 20)
print('total lines:', alllines)
print('total code lines', codelines)
print('total space lines', spacelines)
print('total note lines', notelines)

