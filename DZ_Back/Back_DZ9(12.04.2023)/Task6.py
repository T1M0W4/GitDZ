while True:
    user_word = input("Введите слово с маленькой заглавной буквы: ")
    if user_word.isalpha() == True:   
            break
    else:
        print("Некорректный ввод. Введите слово из букв!")

word = user_word[0]
increase = chr(ord(word) - ord('a') + ord('A')) + user_word[1:]

print("Слово с заглавной буквы:", increase)