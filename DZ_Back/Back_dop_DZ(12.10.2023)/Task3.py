text = input("Введите строку для шифрования: ")

encrypted_text = ""
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for char in text:
    if char in alphabet:
        index = alphabet.index(char)
        encrypted_char = alphabet[(index + 1) % len(alphabet)]
    else:
        encrypted_char = char
    encrypted_text += encrypted_char

print("Зашифрованная строка:", encrypted_text)