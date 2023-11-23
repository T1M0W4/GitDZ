user_word = input("Введите слово из пяти букв: ")

word = user_word.isalpha()

try:
    if word != True:
          raise ValueError()
except ValueError:
    print("Вы ввели не слово!")
    exit()

if len(user_word) > 5 or len(user_word) < 5:
    print("Вы вели либо меньше либо больше пяти букв!")
else:
    if user_word == user_word[::-1]:
        print("Это полиндром!")
    else:
        print("Это не полиндром!")
    