temp_day = input("Введите дневную температуру:")
temp_night = input("Введите ночную температуру:")

temp_day = int(temp_day)
temp_night = int(temp_night)

all_temp = abs(temp_day - temp_night)
print("Перепад:", all_temp)