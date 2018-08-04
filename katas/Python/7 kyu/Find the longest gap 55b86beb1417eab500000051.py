# https://www.codewars.com/kata/55b86beb1417eab500000051
import re


def gap(num):
    return max((len(m.group(1)) for m in re.finditer('(?<=1)(0+)(?=1)', bin(num))), default=0)
    
