num = 1
zero = 0
pos = 0
neg = 0
even = 0
odd = 0

while num <= 10:
    while True:
        try:
            user_num = int(input("Введите первое число: "))
            break
        except ValueError:
            print('некорректный ввод. введите целое число.')
    num +=1            

    if user_num == 0:
        zero += 1
    elif user_num > 0:
        pos += 1
    elif user_num < 0:
        neg += 1
    
    if user_num % 2 == 0:
        even += 1
    else:
        odd += 1
        
print("Общее кол-во положительны(",pos,"), отрицательных(",neg,"), четных(",even,"), нечетных(",odd,") и нулей(",zero,")!", sep="")