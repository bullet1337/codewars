# https://www.codewars.com/kata/56606694ec01347ce800001b
def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a
