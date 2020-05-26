# 10. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Исключить все нулевые элементы.
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(-1, 10))
print(num_list)

new_list = list()
for n in num_list:
    if n != 0:
        new_list.append(n)
print(new_list)
