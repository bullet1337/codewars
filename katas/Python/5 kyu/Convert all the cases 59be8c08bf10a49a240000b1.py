# https://www.codewars.com/kata/59be8c08bf10a49a240000b1
import re

replacements = {
    'snake': lambda m: '_' + m.group()[-1].lower(),
    'camel': lambda m: m.group()[-1].upper(),
    'kebab': lambda m: '-' + m.group()[-1].lower()
}


def change_case(identifier, targetCase):
    if targetCase not in replacements:
        return None
    if identifier:
        x, y, z = '-' in identifier, '_' in identifier, any(c.isupper() for c in identifier)
        if not((x ^ y ^ z) and not (x & y & z)):
            return None

    return re.sub('(?P<kebab>-[a-zA-Z])|(?P<snake>_[a-zA-Z])|(?P<camel>[A-Z])', replacements[targetCase], identifier)
