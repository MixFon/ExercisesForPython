# 3. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Поменять местами элементы, стоящие на чётных и нечётных местах: А[ 1]
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(-10, 10))
print(num_list)

for i in range(len(num_list)):
    if i % 2 != 0:
        temp = num_list[i - 1]
        num_list[i - 1] = num_list[i]
        num_list[i] = temp
print(num_list)
