#6. Дан одномерный массив числовых значений, насчитывающий N элементов.
#Поменять местами группу из М элементов, начинающихся с позиции К с группой
#из М элементов, начинающихся с позиции Р.
import random

n = int(input("Введите колличество элементов массива:\n"))
m = int(input("Соклько элементов группы M?\n"))
k = int(input("С какого номера начинается группа K?\n"))
p = int(input("С какого номера начинается группа P?\n"))
if m < 0 or k <= 0 or p <= 0:
    print("Введенные числа должны быть положительными и больше нуля.")
    exit(0)

# Создание списка со случайными значениями.
num_list = list()
for a in range(n):
    num_list.append(random.randint(-10, 10))
print(num_list)

new_list = num_list[ : k]
new_list += num_list[p : p + m]
new_list += num_list[k + m : p]
new_list += num_list[k : k + m]
new_list += num_list[p + m :]
print(new_list)
