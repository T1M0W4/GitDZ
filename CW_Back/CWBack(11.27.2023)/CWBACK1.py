user_in = input("Введите номер дня недели: ")
try:
    day = int(user_in)
except ValueError:
    print("Вы ввели не число!")
    exit()

match day:
    case 1:
        day_name = "Понедельник"
    case 2:
        day_name = "Вторник"
    case 3:
        day_name = "Среда"
    case 4:
        day_name = "Четверг"
    case 5:
        day_name = "Пятница"
    case 6:
        day_name = "Суббота"
    case 7:
        day_name = "Воскресение"
    case _:
        day_name = "XP"
    




#if day == 1:
#    day_name = "Понедельник"
#elif day == 2:
#    day_name = "Вторник"
#elif day == 3:
#    day_name = "Среда"
#elif day == 4:
#    day_name = "Четверг"
#elif day == 5:
#    day_name = "Пятница"
#elif day == 6:
#    day_name = "Суббота"
#elif day == 7:
#    day_name = "Воскресение"
#else:
#    day_name = "ХЗ"    

#print(day_name)