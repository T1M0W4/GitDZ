# Функция возвращает аббревиатуру от переданной строки
def get_abbr(phrase):
    if phrase == '':
        return ''

    us_list = phrase.split()
    result = ''

    for word in us_list:
        result += (word[0])

    return result.upper()


def test_get_abbr():
    assert get_abbr('семь раз отмерь - один раз отрежь') == 'СРО-ОРО'
    assert get_abbr("don't repeat yourself") == 'DRY'
    assert get_abbr('') == ''
    print("Тест пройден")

test_get_abbr()
