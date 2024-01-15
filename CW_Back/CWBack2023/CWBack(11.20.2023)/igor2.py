user_rad_in = input("Введите радиус окружности: ")

try:
    r = float(user_rad_in)
except ValueError:
    print("Введите положительное дробное число: ")
else:
    square = 3.141597 * r * r

    print("Площадь круга: ", square)