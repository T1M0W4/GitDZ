user_dec_num = int(input("Введите десятичное число: "))

bin_num = bin(user_dec_num)
oct_bum = oct(user_dec_num)
hex_num = hex(user_dec_num)

print("Ваше число в двоичном:", bin_num, "\nВаше число в восьмиричном:", oct_bum, "\nВаше число в шестнадцатиричном:", hex_num)
