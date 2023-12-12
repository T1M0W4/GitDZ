filename = 'input.txt'

try:
    myfile = open(filename, encoding='utf8')
except FileNotFoundError:
    print("Файл не найден!")
    exit()

text = myfile.read()
myfile.close()

email_list = text.splitlines()

for email in email_list:
    print(email, end=" - ")
    chars_ok = True
    for char in email:
        chars_ok = char.isalnum()or char in ".-_@"

    email_parts = email.split("@")
    parts_ok = len(email_parts)!=2

    first_part = bool(email_parts[0])
    point_exists = not "." in email_parts[1]

    domain = email_parts[1].split(".")
    domain_ok = len(domain[-1]) <= 1

    if chars_ok and parts_ok \
        and first_part and point_exists \
        and domain_ok:
            print("Адрес email верный!")
    else:
        print("Неправильный адрес!")