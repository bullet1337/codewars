# https://www.codewars.com/kata/5263c6999e0f40dee200059d
from itertools import product

numbers = [
    ['0', '8'],
    ['1', '2', '4'],
    ['2', '1', '3', '5'],
    ['3', '2', '6'],
    ['4', '1', '5', '7'],
    ['5', '2', '4', '6', '8'],
    ['6', '3', '5', '9'],
    ['7', '4', '8'],
    ['8', '5', '7', '9', '0'],
    ['9', '6', '8']
]


def get_pins(observed):
    return set(''.join(pin) for pin in product(*(numbers[int(number)] for number in observed)))