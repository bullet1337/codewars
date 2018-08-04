# https://www.codewars.com/kata/577e277c9fb2a5511c00001d
def vowel_shift(text, n):
    if not (text and n):
        return text

    indices = [i for i, l in enumerate(text.lower()) if l in 'aioue']
    shifted = list(text)
    for i in range(len(indices)):
        shifted[indices[(i + n) % len(indices)]] = text[indices[i]]
    return ''.join(shifted)