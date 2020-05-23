# 19. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Вместо каждого элемента с нулевым значением поставить сумму двух
# предыдущих элементов массива.
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(0, 5))
print(num_list)
for n in range(len(num_list)):
    if num_list[n] == 0:
        print(num_list[n - 1] + num_list[n - 2], end=' ')
    else:
        print(num_list[n], end=' ')
print()
