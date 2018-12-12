# https://www.codewars.com/kata/559d2284b5bb6799e9000047
def add_length(str_):
    return [s + ' ' + str(len(s)) for s in str_.split()]