filename = 'input1.txt'

try:
    myfile = open(filename, encoding='utf8')
except FileNotFoundError:
    print("Файл не найден!")
    exit()

text = myfile.read()
myfile.close()

print(text)

old_word = input("Введите слова которое хотите заменить: ")
old_word.upper()
old_word.capitalize()

new_word = input("Введите слова которое нужно подставить:")

low_new_word = new_word.lower()
low_old_word = old_word.lower()

res = text.replace(old_word, new_word)

print(res)


