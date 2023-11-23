money = input("Введите сумму в USD: ")

try:
    money = int(money)
except ValueError:
    print("Вы вели не целое число!")
    exit()

user_curr = input("Ведите желаемую валюту из трех(пример: EUR, UAN или AZN): ")

curr = user_curr.isalpha()

try:
    if curr != True:
          raise ValueError()
except ValueError:
    print("Вы ввели не слово!")
    exit()
else:
    if len(user_curr) > 3 or len(user_curr) < 3:
        print("Вы вели либо меньше либо больше трех букв!")
    else:
        if "EUR" in user_curr or user_curr in "EUR":
            trans = money * 0.92
            print("EUR", trans)
        elif "UAN" in user_curr or user_curr in "UAN":
            trans = money * 7.10
            print("UAN", trans)
        elif "AZN" in user_curr or user_curr in "AZN":
            trans = money * 1.70
            print("AZN", trans)
        else:
            print("Вы вели не верно, нужно на англ.языке и большими буквами!")


