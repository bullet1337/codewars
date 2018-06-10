# https://www.codewars.com/kata/5503013e34137eeeaa001648
def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
        
    return '\n'.join(' ' * (abs(i - n // 2)) +'*' * (2 * (-abs(i - n // 2) + n // 2) + 1) for i in range(n // 2 * 2 + 1)) + '\n'