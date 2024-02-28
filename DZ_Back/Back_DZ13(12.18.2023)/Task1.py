def merge_digits(digit1, digit2, digit3):
    merged_number = int(str(digit1) + str(digit2) + str(digit3))
    return merged_number

while True:
    try:
        user_digits1 = input('Введите первую цифру:')
        num1 = int(user_digits1)
        break
    except ValueError:
         print('Некорректный ввод. введите целое число.')
    
while True:
    try:
        user_digits2 = input('Введите вторую цифру:')
        num2 = int(user_digits2)
        break
    except ValueError:
         print('Некорректный ввод. введите целое число.')

while True:
    try:
        user_digits3 = input('Введите третью цифру:')
        num3 = int(user_digits3)
        break
    except ValueError:
         print('Некорректный ввод. введите целое число.')

result = merge_digits(num1, num2, num3)
print(result)