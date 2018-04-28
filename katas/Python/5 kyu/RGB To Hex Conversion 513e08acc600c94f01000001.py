# https://www.codewars.com/kata/513e08acc600c94f01000001
def rgb(r, g, b):
    return ('{:02X}' * 3).format(min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255))