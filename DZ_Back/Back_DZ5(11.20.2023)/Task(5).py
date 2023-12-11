a = input("Введите значение а:")

try:
    a = int(a)
except ValueError:
    print("Вы ввели не целое число!")
    exit()

try:
    b = input("Введите значение b:")
    b = int(b)
except ValueError:
    print("Вы ввели не целое число!")
    exit()    


try:
    b = input("Введите значение b:")
    b = int(b)
except ValueError:
    print("Вы ввели не целое число!")
    exit()    


x = - b/a
#VN: тут может быть исключение, если a равно 0

print("значение х:", x)
