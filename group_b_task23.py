# 23. Заданы М строк символов, которые вводятся с клавиатуры.
# Из заданных строк, каждая из которых представляет одно слово,
# составить одну длинную строку, разделяя слова пробелами.

m = int(input("Введите колличество строк:\n"))
all_string = ""
for a in range(m):
    string = input("Введите строку:\n")
    all_string += " " + string
print(all_string.lstrip(' '))