while True:
    try:
        num = input("Введите целое число сколько смайликов вы хотите: ")
        num = int(num)
        break
    except ValueError:
        print('Некорректный ввод. введите целое число.')

def generate_smiley_string(num):
    return "😊" * num


def test_generate_smiley_string():
    assert generate_smiley_string(3) == "😊😊😊"
    assert generate_smiley_string(5) == "😊😊😊😊😊"
    assert generate_smiley_string(0) == ""
    assert generate_smiley_string(1) == "😊"
    print('Готово!')

test_generate_smiley_string()

print(generate_smiley_string(num))