while True:
    try:
        price = int(input("Введите стоимость покупки: "))
        break
    except ValueError:
        print("Некорректный ввод. введите целое число.")

while True:
    try:
        perc = float(input("Введите стоимость покупки: "))
        break
    except ValueError:
        print("Некорректный ввод. введите целое число.")


disc = price - ((price * perc)/100)
disc = round(disc)

print(f"Стоимость товара со сидкой: {disc}")