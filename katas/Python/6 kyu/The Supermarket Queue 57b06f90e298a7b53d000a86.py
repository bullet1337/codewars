# https://www.codewars.com/kata/57b06f90e298a7b53d000a86
def queue_time(customers, n):
    pool = [0] * n
    for c in customers:
        pool[min(enumerate(pool), key=lambda x: x[1])[0]] += c
    return max(pool)