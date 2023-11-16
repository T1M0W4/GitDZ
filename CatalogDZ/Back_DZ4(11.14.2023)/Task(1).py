temp_day = input("Введите дневную температуру:")
temp_night = input("Введите ночную температуру:")

temp_day = int(temp_day)
temp_night = int(temp_night)

temp_diff = abs(temp_day - temp_night)
print("Перепад температуры:", temp_diff)