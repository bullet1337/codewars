# https://www.codewars.com/kata/53e895e28f9e66a56900011a
from collections import Counter
import re


def letter_frequency(text):
    return sorted(Counter(re.sub(r'[^a-z]', '', text, flags=re.I).lower()).most_common(), key=lambda x: (-x[1], x[0]))