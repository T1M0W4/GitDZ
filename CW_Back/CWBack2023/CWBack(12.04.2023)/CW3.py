user_in = input("Введите слово: ")

vig = len(user_in)
vig = int(vig) - 2
sin = "*" * vig
pro = user_in[0] + sin + user_in[-1]

print(pro)