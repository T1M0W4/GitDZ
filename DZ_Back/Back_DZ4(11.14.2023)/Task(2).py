user_float_num = float(input("Введите дробное число:"))
user_int_num = int(input("Количество дробей:"))

user_round_num = round(user_float_num, user_int_num)

print("Округление:", user_round_num)