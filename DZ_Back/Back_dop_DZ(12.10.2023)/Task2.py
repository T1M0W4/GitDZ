source = input("Введите список чисел через пробел: : ")
source_list = source.split(' ')

numbers = []
try:
    for x in source_list:
        numbers += [int(x)]
except ValueError:
    print("Все введенные данные должны быть целыми числами!")
    exit()

print(numbers)
is_simple = True
result = []
for x in numbers:
    if x <= 0:
        continue
    elif x > 1:
        is_simple = True
        for i in range(2, 1 + x//2):
            if x % i == 0:
                is_simple = False
                break
    if is_simple:
        result.append(x)

print(result)