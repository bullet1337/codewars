# https://www.codewars.com/kata/59325dc15dbb44b2440000af
def is_alt(s):
    first = next((i for i, l in enumerate(s) if l in 'aioue'), None)
    return first is not None and all(l in 'aioue' for l in s[first % 2::2]) and all(l not in 'aioue' for l in s[(first + 1) % 2::2])
    