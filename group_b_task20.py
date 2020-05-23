# 20. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, имеются ли в массиве два подряд идущих нуля.
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(0, 5))

print(num_list)
count = 0
for n in num_list:
    if n == 0:
        count += 1
    if count == 2:
        print("Имеется два подрят идущих нуля.")
        exit(0)
print("Нет двух подрят идущих нуля.")
