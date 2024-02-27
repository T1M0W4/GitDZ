text = input("Введите строку для шифрования: ")
key = int(input("Введите ключ шифрования (целое число): "))

encrypted_text = ""
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for char in text:
    if char in alphabet:
        index = alphabet.index(char)
        encrypted_index = (index + key) % len(alphabet)
        encrypted_char = alphabet[encrypted_index]
    else:
        encrypted_char = char
    encrypted_text += encrypted_char

print("Зашифрованная строка:", encrypted_text)