user_num1 = input("Введите первую калбасу: ")
user_num2 = input("Введите вторую калбасу: ")

try:
    num1 = float(user_num1)
    num2 = float(user_num2)
except ValueError:
    print("Введите целую калбасу")
else:
    try:
        all_num = num1 / num2
    except ZeroDivisionError:
        print("Нельзя делить на 0 калбас")            
    else:
        all_num = num1 / num2
        print("Ваша поделеная калбаса: ", all_num)


