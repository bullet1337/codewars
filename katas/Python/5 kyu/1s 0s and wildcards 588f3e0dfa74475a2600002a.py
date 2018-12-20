# https://www.codewars.com/kata/588f3e0dfa74475a2600002a
import re
from itertools import product, zip_longest


def possibilities(param):
    positions = [m.start() for m in re.finditer('\?', param)]
    param = param.split('?')
    return [''.join(a + b for a, b in zip_longest(param, tuple, fillvalue='')) for tuple in product(*([['0', '1']] * len(positions)))]