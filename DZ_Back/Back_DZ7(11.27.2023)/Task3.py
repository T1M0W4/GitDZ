while True:
    try:
        num1 = int(input("Введите первое число: "))
        break
    except ValueError:
        print('некорректный ввод. введите целое число.')

while True:
    try:
        num2 = int(input("Введите второе число: "))
        break
    except ValueError:
        print('некорректный ввод. введите целое число.')

while num1 != 0 and num2 != 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1
 
print("НОД ваших двух чисел:", num1 + num2)
