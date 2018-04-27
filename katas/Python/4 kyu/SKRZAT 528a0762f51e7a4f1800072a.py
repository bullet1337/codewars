# https://www.codewars.com/kata/528a0762f51e7a4f1800072a
def b2d(binary):
    base_pow = 1
    decimal = 0
    for c in reversed(binary):
        decimal += int(c) * base_pow
        base_pow *= -2
    return decimal


def d2b(decimal):
    binary = ''
    while decimal != 0:
        decimal, mod = divmod(decimal, -2)
        if mod != 0:
            decimal += 1
        binary += str(abs(mod))
    return binary[::-1] or '0'
    
  
def skrzat(base, number):
    return 'From {}: {} is {}'.format(
        'binary' if base == 'b' else 'decimal',
        str(number),
        str(b2d(number) if base == 'b' else d2b(number))
    )