while True:
    word = input("Введите слово: ")
    if word.isalpha() == True:   
            break
    else:
        print("Некорректный ввод. Введите слово из букв!")

print("Это '%s%s-%s%s' сокрощение слова: '%s'" % (word[0], word[1], word[-2], word[-1], word))