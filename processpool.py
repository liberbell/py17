import os
from multiprocessing import Pool

# def cal_square(n):
#     return n * n

def cal_square(n):
    print(n, os.getpid())
    return n * n

num_list = [1, 2, 3, 4, 5]
result = []

for num in num_list:
    result.append(cal_square(num))

print(result)

print(os.cpu_count())