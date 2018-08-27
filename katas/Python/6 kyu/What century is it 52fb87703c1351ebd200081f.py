# https://www.codewars.com/kata/52fb87703c1351ebd200081f
from math import ceil

endings = {
    11: 'th',
    12: 'th',
    13: 'th',
    1: 'st',
    2: 'nd',
    3: 'rd'
}


def whatCentury(year):
    def ending(century):
        return str(century) + endings.get(century, endings.get(century % 10, 'th'))
            
    return ending(ceil(int(year) / 100))