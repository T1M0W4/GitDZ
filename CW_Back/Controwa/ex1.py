# Функция возвращает результат деления большего по модулю числа на меньшее.
def smart_div(num1, num2=None):
    if num2 is None:
        num2 = num1
    
    if abs(num1) < abs(num2):
        num1,num2 = num2,num1
        
    return num1 / num2


def test_smart_div():
    assert smart_div(20, 4) ==  5
    assert smart_div(3, -6) == -2
    assert smart_div(-8)    ==  1
    print("Тест пройден")
    
test_smart_div()
