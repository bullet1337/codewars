# https://www.codewars.com/kata/55466989aeecab5aac00003e
def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    
    squares = []
    x, y = (lng, wdth) if lng < wdth else (wdth, lng)
    while y % x != 0:
        squares.append(x)
        y -= x
        if y < x:
            x, y = y, x
    squares.extend(x for _ in range(y // x))
    return squares