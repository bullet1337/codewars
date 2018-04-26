# https://www.codewars.com/kata/52f831fa9d332c6591000511
from collections import defaultdict


def update_quantity(elements, multiplier):
    multiplier = int(multiplier) if multiplier else 1
    for element, quantity in elements.pop().items():
        elements[-1][element] += quantity * multiplier


def add_element(elements, element, multiplier):
    multiplier = int(multiplier) if multiplier else 1
    elements[-1][element] += multiplier


def parse_molecule(formula):
    elements = [defaultdict(int)]
    element = None
    multiplier = ''
    bracket = False

    for c in formula:
        if c.isupper():
            if bracket:
                update_quantity(elements, multiplier)
                bracket = False
                multiplier = ''

            if element is None:
                element = c
            else:
                add_element(elements, element, multiplier)
                multiplier = ''
                element = c
        elif c.islower():
            element += c
        elif c.isdigit():
            multiplier += c
        elif c == '(' or c == '[' or c == '{':
            if element is not None:
                add_element(elements, element, multiplier)

            if bracket:
                update_quantity(elements, multiplier)
                bracket = False

            elements.append(defaultdict(int))
            element = None
            multiplier = ''
        else:
            if bracket:
                update_quantity(elements, multiplier)

            if element is not None:
                add_element(elements, element, multiplier)

            element = None
            multiplier = ''
            bracket = True
    if element is None:
        if bracket:
            update_quantity(elements, multiplier)
    else:
        add_element(elements, element, multiplier)

    return elements[-1]