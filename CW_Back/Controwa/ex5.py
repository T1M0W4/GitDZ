''' Функция принимает на вход текст, и возвращает словарь, содержащий все слова из этого текста в нижнем регистре в качестве ключей, и количество этих слов в тексте в качестве значений.
'''
def count_words(text: str) -> dict:
    pass


def test_count_words():
    assert count_words("Rocking around a christmas tree") == {"rocking":1, "around":1, "a":1, "crhistmas":1, "tree":1}
    assert count_words("star star Star") == {"star":3}
    assert count_words("") == {}
    assert count_words() == {}
    print("Тест пройден")

test_count_words()

