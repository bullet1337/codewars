# https://www.codewars.com/kata/538ae2eb7a4ba8c99b000439
import re 


def autocorrect(input):
    return re.sub(r'\b(you+|u)\b', 'your sister', input, flags=re.I)
    