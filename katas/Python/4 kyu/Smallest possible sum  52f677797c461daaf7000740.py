# https://www.codewars.com/kata/52f677797c461daaf7000740
def solution(a):
    while len(set(a)) > 1:
        x = min(a)
        for i in range(len(a)):
            mod = a[i] % x
            if mod == 0:
                a[i] = x
            else:
                a[i] = mod
    return sum(a)