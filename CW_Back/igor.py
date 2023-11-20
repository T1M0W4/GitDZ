import math
try:
    user_in1 = input("Ввод первого числа: ")
    user_in2 = input("Ввод второго числа: ")

    user_in1 = int(user_in1)
    user_in2 = int(user_in2)

    diff = user_in1 - user_in2
    result = math.sqrt(diff)

    print("Вы не ебанат: ", result) 
except ValueError:
    print("Вы ебанат!")