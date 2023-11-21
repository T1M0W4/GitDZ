user_dec_num = input("Введите десятичное число: ")

try:
    dec_num = int(user_dec_num)
except ValueError:
    print("Галым, тебя считает тупым! Но я тебя понимаю брат, десятичное выглядит вот так 10 или так 20, вот так 30 и т.п.")
else:
    bin_num = bin(dec_num)
    oct_bum = oct(dec_num)
    hex_num = hex(dec_num)

    print("Ваше число в двоичном:", bin_num, "\nВаше число в восьмиричном:", oct_bum, "\nВаше число в шестнадцатиричном:", hex_num)
