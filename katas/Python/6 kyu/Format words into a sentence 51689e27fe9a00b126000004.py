# https://www.codewars.com/kata/51689e27fe9a00b126000004
def format_words(words):
    if words is None:
        return ''
    
    words = [w for w in words if w]
    if not words:
        return ''
    elif len(words) == 1:
        return words[0]
    else:
        return '{} and {}'.format(', '.join(words[:-1]), words[-1])