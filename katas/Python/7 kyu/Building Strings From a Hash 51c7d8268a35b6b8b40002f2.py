# https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2
def solution(pairs):
    return ','.join('{} = {}'.format(k, v) for k, v in sorted(pairs.items()))