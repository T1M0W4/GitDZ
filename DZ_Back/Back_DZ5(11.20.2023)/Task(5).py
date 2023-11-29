a = input("Введите значение а:")

try:
    a = int(a)
except ValueError:
    print("Вы ввели не целое число!")
    exit()
<<<<<<< HEAD

try:
    b = input("Введите значение b:")
    b = int(b)
except ValueError:
    print("Вы ввели не целое число!")
    exit()    
=======
else:
#VN: если внутри except использовать exit(), то нет смысла писать else. 
# Можно следующий try начинать как отдельную самостоятельную конструкцию.
# Это также касается ваших решений других задач
    try:
        b = input("Введите значение b:")
        b = int(b)
    except ValueError:
        print("Вы ввели не целое число!")
        exit()    
>>>>>>> 53b3a4ffefc116e844fe5be1eba03844e2f0e9ef

x = - b/a

print("значение х:", x)
