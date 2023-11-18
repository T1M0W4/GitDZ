user_in = input("Сколько Вам лет?: ")

user_number = int(user_in)
user_number = pow(user_number, 2)
#^^^^^^^^^^ в этой и следующих работах вы используете переменные, которые "под руку подвернулись"
# давайте переменным осмысленные имена, напрмер:
# squared_number = pow(user_number, 2)

print("Ваш возвраст, возведеная в степень 2 = ", user_number)