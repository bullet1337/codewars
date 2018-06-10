# https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    return sum(stop[0] - stop[1] for stop in bus_stops)