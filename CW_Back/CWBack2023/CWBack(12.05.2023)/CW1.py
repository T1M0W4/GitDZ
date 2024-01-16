user_in = input("Введите числа через пробел: ")
user_data = user_in.split(",")
print(user_data)

numb = []

for i in user_data:
    i = int(i)
    numb.append(int(i))

    
print(numb)