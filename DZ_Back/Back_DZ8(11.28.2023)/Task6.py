while True:
    user_num = input("Введите число: ")
    if user_num.isdigit() == True:   
            break
    else:
        print('Некорректный ввод. Введите целое число.')

while True:
        try:
            user_shift = int(input("Введите количчество сдвигов: "))
            break
        except ValueError:
            print('Некорректный ввод. Введите число.')

shift = 0

for i in range(user_shift):
    shift += 1
    num1 = user_num[1:]
    num2 = user_num[0]
    num3 = num1 + num2
    print("Сдвиг(%s)"% (shift),num3)
    user_num = num3

print("Результат со всеми сдвигами:", num3)
