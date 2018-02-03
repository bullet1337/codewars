# https://www.codewars.com/kata/581e014b55f2c52bb00000f8
import re


def decipher(word):
    code = re.search('^\d+', word).group()
    first = chr(int(code))
    word = word[len(code):]
    return first + (word[-1] + word[1:-1] + word[0] if len(word) > 1 else word)


def decipher_this(string):
    return ' '.join(decipher(word) for word in string.split())