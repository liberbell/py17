import os
from multiprocessing import Pool
import time

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

p = Pool()
result = p.map(cal_square, num_list)
p.close()
print(result)
result = []

p = Pool(processes=2)
result = p.map(cal_square, num_list)
p.close()
print(result)

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s

def sum_square_with_map(numbers):
    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)