#Вводятся положительные числа.
#Определить сумму чисел делящихся на положительное число B нацело.
#При вводе отрицательного число завершить работу.

b = int(input("Введите число B:\n"))
summ = 0
while 1:
    num = int(input("Введите число:\n"))
    if (num < 0):
        print("Cумма чисел делящихся на " + str(b) + " = " + str(summ))
        exit(0)
    if num % b == 0:
        summ += 1
