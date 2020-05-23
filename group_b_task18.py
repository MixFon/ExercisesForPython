# 18. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Исключить из массива элементы, принадлежащие промежутку [В; С].
import random

m = int(input("Введите колличество элементов массива:\n"))
b = int(input("Введите число B:\n"))
c = int(input("Введите число C:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(0, 5))

print(num_list)
new_list = num_list[:b]
new_list += num_list[c:]
print(new_list)
