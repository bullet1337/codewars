# https://www.codewars.com/kata/55c6126177c9441a570000cc
import re


def order_weight(string):
    numbers = re.findall('\d+', string)
    numbers_props = {number: (sum(int(d) for d in number), number) for number in numbers}
    return ' '.join(sorted(numbers, key=lambda x: numbers_props[x]))