# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
def get_count(n, number):
    temp = number
    count = 0
    while n >= number:
        count += n // number
        number *= temp
    return count


def zeros(n):
    return min(get_count(n, 2), get_count(n, 5))