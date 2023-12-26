input  = [3,19,16,14,5]
max = 2
user_list = []

for i in input:
    if i > max:
        input.remove(i)            
    else:
        user_list += i

print input[::-1]