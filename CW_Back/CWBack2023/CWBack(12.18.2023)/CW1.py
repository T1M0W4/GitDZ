
user1 = input("a:")
user2 = input("b:")

try:
    num1 = int(user1)
    num2 = int(user2)
except ValueError:
    print("error")
    exit()

def get_sum(a,b):
    result = a+b
    return result

my_sum = get_sum(num1, num2)
print("Result = %i" % my_sum)