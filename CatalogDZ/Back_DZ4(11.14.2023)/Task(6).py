in_time = float(input("Введите часы и минуты(пример 7.30 или 13.15): "))

time = float(23.60)
time_und = (time-in_time)
time_und2 = str(round(time_und, 4))      

print("Первое число количество часов, второе количество минут до следуйщего дня: ", time_und2.split("."))