# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    x = [n % 2 for n in integers[:3]]
    x = x[0] & x[1] | x[0] & x[2] | x[1] & x[2]
    return next(n for n in integers if n & 1 != x)