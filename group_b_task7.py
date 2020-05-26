# 7. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Вставить группу из М новых элементов, начиная с позиции К.
import random

n = int(input("Введите колличество элементов массива:\n"))
m = int(input("Соклько элементов группы M?\n"))
k = int(input("С какого номера вставлять?\n"))
if m < 0 or k <= 0:
    print("Введенные числа должны быть положительными и больше нуля.")
    exit(0)

# Создание списка со случайными значениями.
num_list = list()
for a in range(n):
    num_list.append(random.randint(0, 10))
print(num_list)

# Создание списка чисел группы М со случайными значениями.
goupM = list()
for b in range(m):
    goupM.append(random.randint(-10, 0))
print(goupM)

new_list = list()
for i in range(len(num_list)):
    if i < k - 1 or i > k + m - 2:
        new_list.append(num_list[i])
    else:
        new_list += goupM
        new_list += num_list[i:]
        break
print(new_list)
