while True:
    try:
        sum_value1 = int(input("Введите первое число: "))
        break
    except ValueError:
        print('некорректный ввод. введите целое число.')

while True:
    try:
        sum_value2 = int(input("Введите второе число: "))
        break
    except ValueError:
        print('некорректный ввод. введите целое число.')


n = sum_value1 + sum_value2
    
print(n)
