# https://www.codewars.com/kata/5434283682b0fdb0420000e6
def caffeineBuzz(n):
    return 'mocha_missing!' if n % 3 != 0 else ('Coffee' if n % 4 == 0 else 'Java') + ('' if n % 2 else 'Script')
