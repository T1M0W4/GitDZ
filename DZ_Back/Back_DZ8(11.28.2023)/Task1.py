while True:
    try:
        sum_val1 = int(input("Введите число которого хотите узнать делитель: "))
        break
    except ValueError:
        print('Некорректный ввод. введите целое число.')

step = -1
div_list = []

for i in range(sum_val1, 0, step):
    div = sum_val1 / step
    step -= 1
    if div != int(div): 
        continue
    
    div_list += [(abs(round(div)))]
    
div_list.pop(0)

print("Ваши делители:", sorted(div_list))
    
     
