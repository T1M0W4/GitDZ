
while True:
    word = input("Введите слово: ")
    if word.isalpha() == True:   
            break
    else:
        print("Некорректный ввод. Введите слово из букв!")

stack = sum(ord(i) for i in word)

print("Сумма кодов символов в слове '%s': (%s)" % (word, stack))