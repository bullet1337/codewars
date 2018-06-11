# https://www.codewars.com/kata/55aa075506463dac6600010d
memo = {}


def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        if i in memo:
            if memo[i]:
                res.append(memo[i])
            continue
            
        sum = 0
        for j in range(1, i + 1):
            if i % j == 0:
                sum += j ** 2
        if (sum ** .5).is_integer():
            res.append([i, sum])
            memo[i] = res[-1]
        else:
            memo[i] = False 
    return res
    