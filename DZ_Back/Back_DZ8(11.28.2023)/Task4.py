zero = 0

while zero == zero:
    print('Программа "Калькулятор" в действии!(Для завершения сеанса, введите два нуля(00)')

    while True:
        try:
            user_num1 = float(input("Введите первое число: "))
            break
        except ValueError:
            print('Некорректный ввод. Введите число.')

    if user_num1 == 00:
        print("Сеанс окончен, спасибо!")
        exit()

    while True:
        user_sign = input("Введите знак('+', '-', '*', '/'): ")
        if user_sign in ('+', '-', '*', '/'):
            break
        elif user_sign in "00":
            print("Сеанс окончен, спасибо!")
            exit()          
        else:
            print("Некорректный ввод.Вы ввели не предложеный программой знак!")

    while True:
        try:
            user_num2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print('Некорректный ввод. Введите число.')

    if user_num2 == 00:
        print("Сеанс окончен, спасибо!")
        exit()

    match user_sign:
            case "+":
                    add = user_num1 + user_num2
                    print("Результат сложения:", add)
            case "-":
                    diff = user_num1 - user_num2
                    print("Результат вычетания:", diff)
            case "*":
                    multiply = user_num1 * user_num2
                    print("Результат умножения:", multiply)
            case "/":
                try:
                    zero = user_num1 / user_num2
                except ZeroDivisionError:
                    print("Нельзя делить на ноль!")
                print("Результат деления:", zero)  
            



