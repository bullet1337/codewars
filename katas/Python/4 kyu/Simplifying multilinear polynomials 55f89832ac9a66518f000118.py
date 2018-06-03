# https://www.codewars.com/kata/55f89832ac9a66518f000118
import re
from collections import defaultdict


def simplify(poly):
    polies = defaultdict(int)
    for m in re.findall('(-?)(\d*)(\w+)', poly):
        polies[''.join(sorted(m[2]))] += (int(m[1]) if m[1] else 1) * (-1 if m[0] else 1)
    simple = ''.join('{}{}{}'.format('+' if count > 0 else '-', abs(count) if abs(count) != 1 else '', poly) for poly, count in sorted(polies.items(), key=lambda x: (len(x[0]), x[0])) if count != 0)
    return simple[simple[0] == '+':]