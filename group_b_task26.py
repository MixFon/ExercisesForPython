# 26. Заданы М строк слов, которые вводятся с клавиатуры
# (в каждой строке одно слово). Вводится слог (последовательность букв).
# Удалить данный слог из каждой строки.

m = int(input("Введите колличество строк:\n"))
for a in range(m):
    string = input("Введите строку:\n")
    sl = input("Введите слог:\n")
    print(string.replace(sl, ''))