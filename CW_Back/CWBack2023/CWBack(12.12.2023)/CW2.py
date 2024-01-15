filename = 'input.txt'

try:
    myfile = open(filename, encoding='utf8')
except FileNotFoundError:
    print("Файл не найден!")
    exit()

text = myfile.readline()
myfile.close()

print(text)