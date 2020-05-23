# 16. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Добавить к элементам массива такой новый элемент, чтобы сумма элементов
# с положительными значениями стала бы равна модулю суммы элементов с
# отрицательными значениями.
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
        neg += n
    else:
        poz += n
print("Модуль суммы отрицательных чисел: " + str(abs(neg)))
print("Суммы положительных чисел: " + str(poz))
diff = abs(neg) - poz
for n in range(len(num_list)):
    num_list[n] += diff
print(num_list)
