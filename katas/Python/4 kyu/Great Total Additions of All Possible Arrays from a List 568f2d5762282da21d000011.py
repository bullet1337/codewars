# https://www.codewars.com/kata/568f2d5762282da21d000011
from itertools import permutations, chain


def gta(limit, *args):
    args = [str(arg) for arg in args]
    base_string = ''
    i = 0
    while len(base_string) < limit:
        for arg in args:
            if i < len(arg) and arg[i] not in base_string:
                base_string += arg[i]
                if len(base_string) == limit:
                    break
        i += 1
    
    args = [int(x) for x in base_string]
    return sum(sum(chain(*permutations(args, i))) for i in range(1, limit + 1))
