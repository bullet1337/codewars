# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
def zero(f=None): return 0 if f is None else f(0)
def one(f=None): return 1 if f is None else f(1)
def two(f=None): return 2 if f is None else f(2)
def three(f=None): return 3 if f is None else f(3)
def four(f=None): return 4 if f is None else f(4)
def five(f=None): return 5 if f is None else f(5)
def six(f=None): return 6 if f is None else f(6)
def seven(f=None): return 7 if f is None else f(7)
def eight(f=None): return 8 if f is None else f(8)
def nine(f=None): return 9 if f is None else f(9)

def plus(arg): return lambda x: x + arg
def minus(arg): return lambda x: x - arg
def times(arg): return lambda x: x * arg
def divided_by(arg): return lambda x: x // arg