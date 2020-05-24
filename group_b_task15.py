# 15. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Добавить столько элементов, чтобы элементов с положительными и
# отрицательными значениями стало бы поровну.
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(-5, 5))
print(num_list)

neg = 0
poz = 0
for n in num_list:
    if n < 0:
        neg += 1
    else:
        poz += 1

diff = neg - poz 
for n in range(abs(diff)):
    if diff < 0:
        num_list.append(-1)
    else:
        num_list.append(1)
print(num_list)
