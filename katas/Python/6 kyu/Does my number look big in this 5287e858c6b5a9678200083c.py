# https://www.codewars.com/kata/5287e858c6b5a9678200083c
def narcissistic(value):
    return value == sum(map(lambda x: int(x) ** len(str(value)), str(value)))