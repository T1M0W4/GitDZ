user_in = input("Введите числа через пробел: ")
user_data = user_in.split(" ")
print(user_data)


for i in range(len(user_data)):
    user_data[i] = int(user_data[i])
print(user_data)
for i in range(len(user_data)):
    user_data[i] +=10
print(user_data)