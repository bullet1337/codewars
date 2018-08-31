# https://www.codewars.com/kata/51e056fe544cf36c410000fb
from collections import Counter
import re


def top_3_words(text):
    return [p[0] for p in Counter(x.lower() for x in re.findall(r'(?!\'[^a-z])[a-z\']+', text, re.I)).most_common(3)]