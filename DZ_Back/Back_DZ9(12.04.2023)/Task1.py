from datetime import datetime

while True:
    while True:
        try:
            day = int(input("Введите день рожднния:"))
            #VN: разделяйте операции ввода данных и их преобразование. input не нужен в try!
            # это у вас во всех задачах.
            break
        except ValueError:
            print("Некорректный ввод. введите целое число.")

    while True:
        try:
            month = int(input("Введите месяц рожднния:"))
            break
        except ValueError:
            print("Некорректный ввод. введите целое число.")

    while True:
        try:
            year = int(input("Введите год рожднния:"))
            break
        except ValueError:
            print("Некорректный ввод. введите целое число.")

    try:
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
            raise ValueError
    except ValueError:
        print(("Некорректная дата"))
    
    try:
        if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
            raise ValueError
    except ValueError:
        print("Некорректный день для данного месяца")
    
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            try:
                if day > 29:
                    raise ValueError
            except ValueError:
                print("Некорректный день для данного месяца")
        else:
            try:
                day > 28
                raise ValueError
            except ValueError:
                print("Некорректный день для данного месяца")
    try:
        if year < 1908:
            raise ValueError
    except ValueError:
        year = 0
        print("Вы не можете быть таким старым!")

    try:
        if year > 2024:
            raise ValueError
    except ValueError:
        year = 11111
        print("Вы не можете родится в будущем!")

    try:
        birth_date = datetime(year, month, day)
        break
    except ValueError:
        print("Пожалуйста, введите корректные значения.")


print("Дата - %s, месяц - %s, и год - %s рождения!" %(day, month, year))