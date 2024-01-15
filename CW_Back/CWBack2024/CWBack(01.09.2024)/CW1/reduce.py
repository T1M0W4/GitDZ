from functools import reduce

array = (5,7,8,3)

result = reduce(lambda acc, x: acc + x, array)
print(result)

text = "Государственая муниципальное унитарное предприятие ромашка"

abbr = reduce(lambda acc, x: acc + x[0].upper(), text.split(), '')
print(abbr)