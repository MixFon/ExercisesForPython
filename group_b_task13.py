# 13. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, образуют ли элементы массива, расположенные перед первым
# отрицательным элементом, убывающую последовательность.
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(-1, 10))
print(num_list)

i = 0
for n in num_list:
    if n < 0:
        while i > 0:
            if num_list[i] > num_list[i - 1]:
                print("No")
                exit(0)
            i -= 1
        print("Yes")
        exit(0)
    i += 1
