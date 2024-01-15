from functools import reduce

numbers = (5, 6, -8, 33, -5)

num = list(map(lambda x: -x, numbers))
print(num)

num1 = list(filter(lambda x: x%2 == 0, numbers))
print(num1)

result = reduce(lambda acc, x: acc * x, num1)
print(result)