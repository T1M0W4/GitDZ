lst = [3, 9, 8, 4, 5, 1]

mn = lst.index(min(lst))
mx = lst.index(max(lst))
lst[mn], lst[mx] =  lst[mx], lst[mn]

print(lst)

# В списке найти минимальный и максимальный элементы, поменять их местами.
