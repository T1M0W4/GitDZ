def get_sum_to(num):
    if num == 1:
        return 1
    return num + get_sum_to(num-1) 

res = get_sum_to(6)
print(res)
