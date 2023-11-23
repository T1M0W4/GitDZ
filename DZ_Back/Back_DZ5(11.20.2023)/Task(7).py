thre_dig_num = input("Введите трехзначное число: ")

try:
    tdn = int(thre_dig_num)
except ValueError:
    print("Вы ввели не число!")
    exit()
else:
    try:
        if tdn < 100 or tdn > 999:
            raise ValueError()
    except ValueError:
        print("Вы ввели не целое трехзначное число!")
        exit()

sec_num = tdn // 10 % 10

print("Вторая цифра вашего числа: ", sec_num)
