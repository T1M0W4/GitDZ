oper = 0

while True:
    try:
        user_num = int(input("Введите первое число: "))
        break
    except ValueError:
        print('некорректный ввод. введите целое число.')

while user_num >= 50:
    user_num /=  2
    oper += 1

print("Ваше полученое число (", user_num, ") и количество операций деления на 2 (", oper,")", sep="")