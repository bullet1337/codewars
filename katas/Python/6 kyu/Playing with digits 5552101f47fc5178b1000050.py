# https://www.codewars.com/kata/5552101f47fc5178b1000050
def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += pow(int(c), p)
        p += 1
    k = sum / n
    return k if k.is_integer() else -1