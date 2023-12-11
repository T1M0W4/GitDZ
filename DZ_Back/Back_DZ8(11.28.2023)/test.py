s = 0

while True:
    s+=1
    try:
        user_fib = int(input("Номер элемента ряда Фибоначчи: "))
        break
    except ValueError:
        print('Некорректный ввод. введите целое число.',(s))
