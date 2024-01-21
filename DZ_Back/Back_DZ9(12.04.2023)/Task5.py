while True:
    c1 = input("Введите символ 'C1': ")
    if len(c1) == 1 and not c1.isalnum():
        break
    else:
        print("Некорректный ввод. Введите спец.символ!")

while True:
    c2 = input("Введите символ 'C1': ")
    if len(c2) == 1 and not c2.isalnum():
        break
    else:
        print("Некорректный ввод. Введите спец.символ!")

while True:
        try:
            length = int(input("Введите длину строки: "))
            break
        except ValueError:
            print("Некорректный ввод. введите целое число.")

result = (c1 + c2) * (length // 2) + c1 * (length % 2)

print("Ваша строка длинной(%s): %s" % (length, result))

