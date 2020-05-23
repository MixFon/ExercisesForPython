# 22. Заданы М строк символов, которые вводятся с клавиатуры.
# Найти количество символов в самой длинной строке.
# Выровнять строки по самой длинной строке, поставив перед каждой
# строкой соответствующее количество звёздочек.

m = int(input("Введите колличество строк:\n"))
dict_string = dict()
max_len = 0
for a in range(m):
    string = input("Введите строку:\n")
    len_str = len(string)
    dict_string[len_str] = string 
    if max_len < len_str:
        max_len = len_str
for key, value in dict_string.items():
    print("*" * (max_len - key) + value)
