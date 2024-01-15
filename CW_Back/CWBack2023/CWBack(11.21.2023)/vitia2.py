User_in = input("")

try:
    num = int(User_in)
except ValueError:
    print("")
else:
    if  num > 0:
        print("Положительное")
    elif num < 0:
        print()
    else:
        print("")   