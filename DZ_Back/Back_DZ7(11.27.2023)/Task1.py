user_num = input("Введите число от 0 до 9: ")

if len(user_num) > 1:
    print("Вы ввели больше чисел, или это вовсе не числа!")
try:
    num = int(user_num)
except ValueError:
    print("Вы ввели не число от 0 до 9!")
    exit()

match num:
    case 0:
        print(")")
    case 1:
        print("!")
    case 2:
        print("@")
    case 3:
        print("#")
    case 4:
        print("$")
    case 5:
        print("%")
    case 6:
        print("^")
    case 7:
        print("&")
    case 8:
        print("*")
    case 9:
        print("(")