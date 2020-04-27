# from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import time

def return_after_n_secs(n, message):
    time.sleep(n)
    return message

pool = ThreadPoolExecutor(3)
submitted_job = pool.submit(return_after_n_secs, 10, "Hello")

print(submitted_job.done())
print(submitted_job.result())
print(submitted_job.done())