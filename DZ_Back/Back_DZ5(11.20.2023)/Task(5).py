a = input("Введите значение а:")

try:
    a = int(a)
except ValueError:
    print("Вы ввели не целое число!")
    exit()
else:
    try:
        b = input("Введите значение b:")
        b = int(b)
    except ValueError:
        print("Вы ввели не целое число!")
        exit()    

x = - b/a

print("значение х:", x)
