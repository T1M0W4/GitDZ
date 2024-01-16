user_in = input("Введите число: ")

int_us = len(user_in) // 2

fir = int(user_in[:int_us])
las = int(user_in[int_us:])

print(fir+las)