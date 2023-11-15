user_coord_x1 = (input("Введите кординаты x1: "))
user_coord_y1 = (input("Введите кординаты y1: "))
user_coord_x2 = (input("Введите кординаты x2: "))
user_coord_y2 = (input("Введите кординаты y2: "))

x1 = int(user_coord_x1)
y1 = int(user_coord_y1)
x2 = int(user_coord_x2)
y2 = int(user_coord_y2)

distance = ((x1-x2)**2+(y1-y2)**2)**0.5

print("Растояние:", distance)