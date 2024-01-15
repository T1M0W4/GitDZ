array = ["Тимур","Аргын","Сергей","Алмат","Вячеслав","Александр","Галымжан","Виталий"]

result = filter(lambda x: len(x) > 8, array)

result = filter(lambda x: x[0] < 'Л', array)

print(list(result))