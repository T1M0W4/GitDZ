temp_day = input("Введите дневную температуру:")
temp_night = input("Введите ночную температуру:")

try:
    temp_d_num = int(temp_day)
    temp_n_num = int(temp_night)
except ValueError:    
    print("Вы ввели не целое число!")
else:    
    temp_diff = abs(temp_d_num - temp_n_num)
    print("Перепад температуры:", temp_diff)
finally:
    print("Благодарим Вас, за использование нашего приложение. Приятного времени суток!")