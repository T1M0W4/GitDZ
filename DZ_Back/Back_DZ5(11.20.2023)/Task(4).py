user_coord_x1 = input("Введите кординаты x1: ")

try:
    x1 = int(user_coord_x1)
except ValueError:
    print("Вы ввели в кординат x1, не целое число!")
else:        
    try:
        user_coord_y1 = input("Введите кординаты y1: ")
        y1 = int(user_coord_y1)
    except ValueError:
        print("Вы ввели в кординат y1, не целое число!")
    else:
        try:
            user_coord_x2 = input("Введите кординаты x2: ")
            x2 = int(user_coord_x2)
        except ValueError:
            print("Вы ввели в кординат x2, не целое число!")
        else:
            try:
                user_coord_y2 = input("Введите кординаты y2: ")
                y2 = int(user_coord_y2)
            except ValueError:
                print("Вы ввели в кординат y2, не целое число!")
            else:
                distance = ((x1-x2)**2+(y1-y2)**2)**0.5

                print("Растояние:", distance)