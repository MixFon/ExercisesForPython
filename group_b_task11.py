# 11. Дан одномерный массив числовых значений, насчитывающий N элементов.
# После каждого отрицательного элемента вставить новый элемент,
# равный квадрату этого отрицательного элемента.
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(-10, 10))
print(num_list)

for i in range(len(num_list)):
    if num_list[i] < 0:
        num_list[i] = num_list[i]**2
print(num_list)
