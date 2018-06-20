import random

def make_number(num, length):
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    a = []
    for i in range(num):
        s = ''
        for j in range(length):
            s += random.choice(str)
        if s not in a:
            a.append(s)
            print(s)
    return a


list = (make_number(20,20))
with open("randomkey.txt", 'w') as file:
    for line in list:
        file.write(line+'\n')

