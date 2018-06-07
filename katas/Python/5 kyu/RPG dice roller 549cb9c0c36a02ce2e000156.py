# https://www.codewars.com/kata/549cb9c0c36a02ce2e000156
import re


def roll(desc, verbose=False):
    if not isinstance(desc, str):
        return False
        
    x = re.fullmatch('(?P<A>\d*)d(?P<X>\d+)(?P<modifier>( *[+-]\d+)*)', desc)
    if x is None:
        return False
    
    result = {}
    result['modifier'] = eval(x.group('modifier') or '0')
    result['dice'] = [max(result['modifier'], 1)] * int(x.group('A') or 1)
    if verbose:
        return result
    else:
        return sum(result['dice']) + result['modifier']
    
