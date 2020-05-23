#Для вводимых чисел определить проент положительных и отрицательных
#При вводе сичла -65432 закончить работу 

posit = 0
negat = 0
count = 0
while 1:
    num = int(input("Введите число:\n"))
    if num == -65432:
        print('Положительные ' + str(round(posit / count * 100, 2)) + '%' )
        print('Положительные ' + str(round(negat / count * 100, 2)) + '%' )
        exit() ;
    if num > 0:
        posit += 1
        count += 1
    else:
        negat += 1
        count += 1



