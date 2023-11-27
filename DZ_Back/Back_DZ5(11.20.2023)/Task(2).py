user_float_num = input("Введите дробное число:")

try:
    float_num = float(user_float_num)
except ValueError:
    print("Вы ввели не дробное число!")
else:
    try:
        user_int_num = input("Количество дробей в целом числе:")
        #VN: ^^^^^^^^^^^^^^^^^ эта строка в блоке try не нужна - она не вызывает исключения
        
        int_num = int(user_int_num)
    except ValueError:
        print("Вы ввели не целое число!")
    else:
        user_round_num = round(float_num, int_num)

        print("Округление:", user_round_num)
    
    
   