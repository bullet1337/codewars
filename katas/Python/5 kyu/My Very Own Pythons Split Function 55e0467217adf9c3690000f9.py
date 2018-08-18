# https://www.codewars.com/kata/55e0467217adf9c3690000f9
def my_very_own_split(string, delimiter=None):
    if delimiter == '':
        raise ValueError()
        
    i = last = 0
    if delimiter is None:
        while i < len(string):
            if string[i].isspace():
                yield string[last:i]
                while i < len(string) and string[i].isspace():
                    i += 1
                last = i
            i += 1
    else:
        while i < len(string):
            if string[i:i + len(delimiter)] == delimiter:
                yield string[last:i]
                i += len(delimiter)
                last = i
            else:
                i += 1
    yield string[last:]
                
                
