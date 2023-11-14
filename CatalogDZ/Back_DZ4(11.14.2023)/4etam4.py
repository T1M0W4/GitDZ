user_float_num = input("Введите дробное число:")
user_int_num = input("Введите число:")

user_float_num = float(user_float_num)
user_int_num = int(user_int_num)

user_round_num = round(user_float_num, user_int_num)

print("Ваше число:", user_round_num)