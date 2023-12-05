user_list = []




while len(user_list) > 10 or len(user_list) < 10:
    user_in = input("")
    user_list = user_in.split(" ")
    if user_list > len(10):
        pressF = user_list[10:]

print(pressF)