# https://www.codewars.com/kata/525f50e3b73515a6db000b83
def create_phone_number(n):
    return '({}) {}-{}'.format(*[''.join(str(x) for x in a) for a in [n[:3], n[3:6], n[6:]]]) 