# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
def fib(n):
    if n == 0:
        return 0
        
    coef = 1 if n >= 0 or n % 2 else -1
    n = abs(n)
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2 * coef
