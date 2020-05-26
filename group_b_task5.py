# 5. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Поменять местами первую и вторую половины массива.
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(-10, 10))
print(num_list)

middle = int(len(num_list) / 2)
num_list = num_list[middle: ] + num_list[:middle]
print(num_list)
