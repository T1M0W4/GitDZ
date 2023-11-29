user_purch = input("На какую сумму, вы хотите совершить покупку?: ")

try:
    purch = int(user_purch)
except ValueError:
    print("Вы ввели не целое число!")
else:
    if purch < 200:
        print("Сумма оплаты без скидки!", purch)
    elif 300 > purch >= 200: 
        disc = (purch*3)/100
        stat = purch - disc 
        print("Сумма оплаты со скидкой в 3%:", stat)
    elif 500 > purch >= 300:
        disc = (purch*5)/100
        stat = purch - disc
        print("Сумма оплаты со скидкой в 5%:", stat)
    elif purch >= 500:
        disc = (purch*7)/100
        stat = purch - disc
        print("Сумма оплаты со скидкой в 7%:", stat)
   

   #VN: подумайте, можно ли в if-elif-else делать вычисления, а print уже делать один, после всего блока?