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


list = (make_number(200,10))


import mysql.connector

def store_mysql():
    conn = mysql.connector.connect(host='localhost', user = 'root', password = '', database= 'ShowMeTheCode', charset='utf8')
    cursor = conn.cursor()

    cursor.execute('show tables in ShowMeTheCode;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
    if not findtables:
        cursor.execute('''
                CREATE TABLE `ShowMeTheCode`.`code` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `code` VARCHAR(10) NOT NULL,
                PRIMARY KEY (`id`));
        ''')

    for line in list:
        code = line.strip()
        print(code)
        cursor.execute("insert into ShowMeTheCode.code(code) values(%s);", [code])
    conn.commit()
    cursor.close()
    conn.close()




if __name__ == '__main__':
    store_mysql()
