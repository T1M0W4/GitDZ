sum1 = 0
sum2 = 0

while True:
    try:
        sum_val1 = int(input("Введите первое число: "))
        break
    except ValueError:
        print('некорректный ввод. введите целое число.')

while True:
    try:
        sum_val2 = int(input("Введите второе число: "))
        break
    except ValueError:
        print('некорректный ввод. введите целое число.')

if sum_val2 < sum_val1:
    b_sum_val = sum_val2
    sum_val2 = sum_val1
    sum_val1 = b_sum_val

while sum_val1 <= sum_val2:
    sum1 = sum_val1
    sum2 += sum1
    sum_val1 += 1

print("Ваша подсчитаная сумма всех чисел в деапозоне:", sum2)
