# https://www.codewars.com/kata/557e8a141ca1f4caa70000a6
def is_triangle_number(number):
    if not isinstance(number, int):
        return False
        
    return ((8 * number + 1) ** .5).is_integer()
    