# https://www.codewars.com/kata/520446778469526ec0000001
def same_structure_as(original,other):
    if type(original) != type(other) or len(original) != len(other):
        return False

    for a, b in zip(original, other):
        if type(a) != type(b) and (type(a) == list or type(b) == list) \
                or type(a) == list and (len(a) != len(b) or not same_structure_as(a, b)):
            return False

    return True
