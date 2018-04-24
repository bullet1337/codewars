# https://www.codewars.com/kata/526a569ca578d7e6e300034e
def convert(input, source, target):
    source_base = len(source)
    source_map = {c: i for i, c in enumerate(source)}
    input = sum(pow(source_base, i) * source_map[c] for i, c in enumerate(reversed(input)))

    target_base = len(target)
    result = ''
    while input > 0:
        input, mod = divmod(input, target_base)
        result += target[mod]
    return result[::-1] or target[0]