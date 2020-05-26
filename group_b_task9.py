# 9. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Исключить из него М элементов, начиная с позиции К.
import random

n = int(input("Введите колличество элементов массива:\n"))
m = int(input("Соклько элементов исключить?\n"))
k = int(input("С какого номера исключать?\n"))
if m < 0 or k <= 0:
    print("Введенные числа должны быть положительными и больше нуля.")
    exit(0)

# Создание списка со случайными значениями.
num_list = list()
for a in range(n):
    num_list.append(random.randint(-1, 10))
print(num_list)

new_list = list()
for i in range(len(num_list)):
    if i < k - 1 or i > k + m - 2:
        new_list.append(num_list[i])
print(new_list)
