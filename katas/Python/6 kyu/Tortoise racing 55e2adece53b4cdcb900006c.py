# https://www.codewars.com/kata/55e2adece53b4cdcb900006c
def race(v1, v2, g):
    if v1 >= v2:
        return None 
    else:
        t = int(g * 3600 / (v2 - v1))
        return [t // 3600, t // 60 % 60, t % 60]