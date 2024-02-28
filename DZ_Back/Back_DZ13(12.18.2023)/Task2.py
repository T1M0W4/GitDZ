def calculate_area(length=None, width=None):
    if width is None:
        area = length ** 2
    elif length is None:
        area = width ** 2
    elif length is None and width is None:
        return 
    else:
        area = length * width
    return area


while True:
    user_length = input('Введите длину прямоугольника:')
    if user_length == '':
        num1 = None
        break
    try:
        num1 = int(user_length)
        break
    except ValueError:
         print('Некорректный ввод. введите целое число.')

while True:
        user_width = input('Введите ширину прямоугольника:')
        if user_width == '':
            num2 = None
            break
        try:
            num2 = int(user_width)
            break
        except ValueError:
            print('Некорректный ввод. введите целое число.')   

if num1 == None or num2 == None:
    square_area = calculate_area(num1)
    print("Площадь квадрата:", square_area)
elif num1 == None and num2 == None:
    print('KEK')
else:
    rectangle_area = calculate_area(num1, num2)
    print("Площадь прямоугольника:", rectangle_area)
