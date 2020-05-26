# 8. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Сумму элементов массива и количество положительных элементов поставить
# на первое и второе место.
import random

n = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(n):
    num_list.append(random.randint(-10, 10))
print(num_list)

count = 0
for n in num_list:
    if n > 0:
        count += 1
summ = sum(num_list)
num_list.insert(0, count)
num_list.insert(0, summ)
print(num_list)
