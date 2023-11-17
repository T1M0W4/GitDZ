temp_day = int(input("Введите дневную температуру:"))
temp_night = int(input("Введите ночную температуру:"))

temp_diff = abs(temp_day - temp_night)
print("Перепад температуры:", temp_diff)