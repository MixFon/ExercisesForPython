# 4. Дан одномерный массив числовых значений, насчитывающий N элементов.
# Выполнить перемещение элементов массива по кругу вправо, т.е.
# А[1]—►А[2];А[2]-►А[3]...А[п]->А[1].
import random

m = int(input("Введите колличество элементов массива:\n"))

# Создание списка со случайными значениями.
num_list = list()
for a in range(m):
    num_list.append(random.randint(-10, 10))
print(num_list)

new_list = list()
new_list.append(0)
for i in range(1, len(num_list)):
    new_list.append(num_list[i - 1])
new_list[0] = num_list[len(num_list) - 1]
print(new_list)
