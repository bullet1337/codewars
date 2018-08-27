# https://www.codewars.com/kata/54b679eaac3d54e6ca0008c9
def create_iterator(func, n):
    def f(m, n=n):
        while n > 0:
            m = func(m)
            n -= 1
        return m
    return f
    