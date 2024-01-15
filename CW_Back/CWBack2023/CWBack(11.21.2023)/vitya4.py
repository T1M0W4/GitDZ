user_hours = input("1")

try:
    hours = int(user_hours)
    hours = 0 < hours < 23
except ValueError:
    print("2")
else:
    try:
        user_min = input("3")
        min = int(user_min)
        min = 0 < min < 59
    except ValueError:
        print("4")
    else:
        try:
            user_sec = input("5")
            sec = int(user_sec)
            sec = 0 < sec < 59
        except ValueError:
            print("6")
        else:
            if hours > 23 and min > 59 and sec > 59:
                print("7")
            elif hours < 00 and min < 00 and sec < 00:
                print("8")
            else:
                print("9" ,hours ,min ,sec)        

