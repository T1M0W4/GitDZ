while True:
        try:
            user_in = int(input("Введите натуральное число: "))
            break
        except ValueError:
            print('Некорректный ввод. Введите натуральное число.')
            
it = 0


while user_in > 1:
    if user_in % 2 != 0:
        user_in = (3 * user_in + 1)
    else:
        user_in /= 2
            
    it += 1
    print(int(user_in))

print("Значение «1» достигнуто за",it, "итераций")