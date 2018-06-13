# https://www.codewars.com/kata/54d418bd099d650fa000032d
def vampire_test(x, y):
    return sorted(str(x) + str(y)) == sorted(str(x * y))