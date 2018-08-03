# https://www.codewars.com/kata/552e45cc30b0dbd01100001a
import re


def zipvalidate(postcode):
    return re.match('[12346]\d{5}$(?!\n)', postcode) is not None