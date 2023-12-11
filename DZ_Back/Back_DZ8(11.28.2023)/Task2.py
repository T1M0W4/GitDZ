fib1 = fib2 = 1
fib0 = 0

while True:
    try:
        user_fib = int(input("Номер элемента ряда Фибоначчи: "))
        break
    except ValueError:
        print('Некорректный ввод. введите целое число.')

 
print(fib0,fib1, fib2, end=' ')
 
for i in range(2, user_fib):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')