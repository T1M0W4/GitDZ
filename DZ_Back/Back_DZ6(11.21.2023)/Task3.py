user_year = input("Введите год: ")

try:
    year = int(user_year)
except ValueError:
    print("Вы ввели не целое число!")
    exit()

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("Год високосный!")
else:
    print("Год не вискосный!")    