employees = ["Иван", "Мария", "Петр", "Анна", "Мария", "Алексей", "Иван"]

double = []

for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        if employees[i] == employees[j] and employees[i] not in double:
            double.append(employees[i])

if double:
    print("Следующие сотрудники получили премию дважды:")
    for d in double:
        print(d)
else:
    print("Никто из сотрудников не получил премию дважды.")


# В массива хранятся имена сотрудников, которым была выписана премия за месяц. Проверить, не попал ли кто-либо из сотрудников в эту базу дважды. Вывести имена этих наглецов)