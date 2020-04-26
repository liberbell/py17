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

def sum_square_with_mp(numbers):
    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)

    p.close()
    p.join()

    total_time = time.time() - start_time
    print("Processing %d numbers took %.2f seconds with using multiprocessing" % (len(numbers), total_time))

def sum_square_without_mp(numbers):
    start_time = time.time()

    result = []
    for i in numbers:
        result.append(sum_square(i))

    total_time = time.time() - start_time
    print("Processing %d numbers took %.2f seconds with using serial processing" % (len(numbers), total_time))

numbers = range(10000)
sum_square_with_mp(numbers)
sum_square_without_mp(numbers)