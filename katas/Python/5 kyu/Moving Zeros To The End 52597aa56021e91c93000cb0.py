# https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(array):
    tmp = [x for x in array if isinstance(x, bool) or not isinstance(x, (float, int)) or x != 0]
    return tmp + [0] * (len(array) - len(tmp))