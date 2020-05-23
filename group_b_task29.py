# 29. Задана строка символов, в которой встречается символ «.».
# Поставить после каждого такого символа системное время ПК.

import datetime

string = input("Введите строку :\n")
for c in string:
    if c == '.':
        print(datetime.datetime.time(datetime.datetime.now()), end="")
    else:
        print(c, end='')
