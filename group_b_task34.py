# Даны число Р и число Н. Определить сумму чисел меньше Р, произведение
# чисел больше Н и количество чисел в диапазоне значений Р и Н.
# При вводе числа равного Р или H, закончить работу.

p = int(input("Введите число P:\n"))
h = int(input("Введите число H:\n"))
summ = 0
mult = 1
count = 0
while 1:
    num = int(input("Введите число:\n"))
    if num == p or num == h:
        print("Сумма чисел меньше P : " + str(summ))
        print("Произведение чисел больше H : " + str(mult))
        print("Колличество чисел от P до H : " + str(count))
        exit(0)
    if num < p:
        summ += num
    if num > h:
        mult *= num
    if num > p and num < h:
        count += 1
