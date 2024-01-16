while True:
    c1 = input("Введите символ 'C1': ")
    if c1.isalpha() == False and c1.isalnum() == False:
        break
    else:
        print("Некорректный ввод. Введите спец.символ!")
    

c2 = input("Введите символ 'C2': ")