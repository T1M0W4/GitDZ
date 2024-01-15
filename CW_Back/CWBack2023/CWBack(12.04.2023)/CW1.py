user_in = input("Введите слово: ")

pol = len(user_in) // 2

first = user_in[:pol]
last = user_in[pol:]

print(first, last)