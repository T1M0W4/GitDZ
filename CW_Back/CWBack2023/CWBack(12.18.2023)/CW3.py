def get_sum_to(num):
    pop = 0
    for i in range(1, num+1):
        pop += i
    return pop 

res = get_sum_to(9)
print(res)