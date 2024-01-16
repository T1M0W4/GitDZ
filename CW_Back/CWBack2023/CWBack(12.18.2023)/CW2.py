
def compare(a,b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

user1 = int(input("num1:"))
user2 = int(input("num2:"))

prop = compare(user1,user2)

print(prop)