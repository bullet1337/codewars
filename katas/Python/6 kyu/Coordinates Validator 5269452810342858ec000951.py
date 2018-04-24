# https://www.codewars.com/kata/5269452810342858ec000951
import re


def is_valid_coordinates(coordinates):
    x = re.fullmatch('(-?\d{1,2}(\.\d+)?), (-?\d{1,3}(\.\d+)?)', coordinates)
    if x is None:
        return False

    return -90 <= float(x.group(1)) <= 90 and -180 <= float(x.group(3)) <= 180