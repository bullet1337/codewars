# https://www.codewars.com/kata/51e0007c1f9378fa810002a9
def parse(data):
    res = []
    var = 0
    for c in data:
        if c == 'i':
            var += 1
        elif c == 'd':
            var -= 1
        elif c == 's':
            var *= var
        elif c == 'o':
            res.append(var)
    return res