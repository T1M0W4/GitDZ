user_rad_in = input("Введите радиус окружности: ")

try:
    rad = float(user_rad_in)
except ValueError:
    print("Вы ввели не число!")
    exit()

user_squ_in = input("Ведите периметр квадрата:")

try:
    squ = int(user_squ_in)
except ValueError:
    print("Вы ввели не положительное целое число!")

half_squ = (squ/4)/2

half_rad = 3.141597/rad/rad

if half_rad > half_squ:
    print("Не помещается!")
elif half_rad <= half_squ:
    print("Помещается!")
else:
    print("Вы ввели отрицательное число!")

   