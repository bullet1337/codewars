# https://www.codewars.com/kata/5262119038c0985a5b00029f
def is_prime(num):
    num = abs(num)
    if num < 2:
        return False
    
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True