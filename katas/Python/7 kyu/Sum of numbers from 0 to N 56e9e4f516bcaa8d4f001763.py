# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763
def show_sequence(n):
    return '{} = {}'.format('+'.join(str(x) for x in range(n+1)), sum(range(n + 1))) if n > 0 else '0=0' if n == 0 else '{}<0'.format(n)