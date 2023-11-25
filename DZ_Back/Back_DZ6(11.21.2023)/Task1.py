user_num = input("Введите число от 0 до 9: ")

if len(user_num) > 1:
    print("Вы ввели больше чисел, или это вовсе не числа!")
try:
    num = int(user_num)
except ValueError:
    print("Вы ввели не число от 0 до 9!")
    exit()
else:
    if num == 0:
        print(")")
    elif num == 1:
        print("!")
    elif num == 2:
        print("@")
    elif num == 3:
        print("#")
    elif num == 4:
        print("$")
    elif num == 5:
        print("%")
    elif num == 6:
        print("^")
    elif num == 7:
        print("&")
    elif num == 8:
        print("*")
    elif num == 9:
        print("(")
    
        