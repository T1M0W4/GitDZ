array = ["Тимур","Аргын","Сергей","Алмат","Вячеслав","Александр","Галымжан","Виталий"]

new_array = sorted(array, key=lambda a: a[-1])
print(new_array)

result = list(map(lambda x: x[-1], array))
print(result)

user_list = []