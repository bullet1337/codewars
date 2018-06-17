# https://www.codewars.com/kata/5421c6a2dda52688f6000af8
def compose(f, g):
    return lambda *args: f(g(*args))