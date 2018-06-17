# https://www.codewars.com/kata/53e30ec0116393fe1a00060b
def unique(integers):
    result = []
    for c in integers:
        if c not in result:
            result.append(c)
    return result