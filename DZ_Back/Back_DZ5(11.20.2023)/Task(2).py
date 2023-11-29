user_float_num = input("Введите дробное число:")

try:
    float_num = float(user_float_num)
except ValueError:
    print("Вы ввели не дробное число!")
    exit()

user_int_num = input("Количество дробей в целом числе:")

try:
    int_num = int(user_int_num)
except ValueError:
    print("Вы ввели не целое число!")
    exit()


user_round_num = round(float_num, int_num)

print("Округление:", user_round_num)
    
    
   