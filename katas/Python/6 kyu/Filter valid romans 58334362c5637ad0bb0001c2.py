# https://www.codewars.com/kata/58334362c5637ad0bb0001c2
import re


def valid_romans(arr):
    return [e for e in arr if re.fullmatch(r'(?=.)(?:M*C?M)?(?:(?<!CM)C?D)?(?:(?<!CD(?=C))C{,3}X?C)?(?:(?<!XC)X?L)?(?:X{,3}I?X)?(?:(?<!IX)(?:IV|V?I{,3}))?', e)]