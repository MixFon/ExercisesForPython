#Ссумировать числа, среди которых нет нулевых (заканчивающихся на ноль)
#При вводе нуля обеспечить вывод текущего значения суммы.
#При вводе числа 99999 закончить работу.

summ = 0;
while 1:
    num = int(input("Введите число:\n"))
    if num == 99999:
        exit(0)
    if num == 0:
        print("Сумма чисел = " + str(summ))
    if num % 10 != 0:
        summ += num
