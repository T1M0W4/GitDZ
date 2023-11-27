user_num = input("Введите трехзначное число: ")

try:
    num = int(user_num)
except ValueError:
    print("Вы ввели не трехзначное целое число!")
    exit()
else:
    try:
        if num < 99 or num > 999:
            raise ValueError()
        #VN: здорово, что вы узнали как бросать исключения
        # здесь, конечно, можно обойтись и без этого
    except ValueError:
        print("Вы ввели либо меньше трехзначного числа либо больше!")
        exit()
    else:
        num1 = num // 100
        num2 = num // 10 % 10
        num3 = num % 10

if num1 == num2 or num2 == num3 or num3 == num1:
    print("Найдено совпадение чисел!")
else:
    print("Совпадений чисел не найдено!")

