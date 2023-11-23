user_sal = int(input("Введите общую сумму продаж за месяц: "))

def_salary = 100
try:
    sales = int(user_sal)
except ValueError:
    sales =def_salary
    print("Знвчение продаж выбрано по-молчанию.")


salary = sales * 0.1 + 250
print("Ваша полная зарплата: ", salary, "$")