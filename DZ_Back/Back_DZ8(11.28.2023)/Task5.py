while True:
    user_num = input("Введите число: ")
    if user_num.isdigit() == True:   
            break
    else:
        print('Некорректный ввод. Введите целое число.')

big_num = "0"
lit_num = "9"

for i in user_num:

    if i >= big_num:
        big_num = i

        
    if i <= lit_num:
        lit_num = i
        
        
print("Ваше наибольшие число: ", big_num)
print("Ваше наименьшее число: ", lit_num)