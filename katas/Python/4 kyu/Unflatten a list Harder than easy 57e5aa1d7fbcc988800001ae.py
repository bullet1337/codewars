# https://www.codewars.com/kata/57e5aa1d7fbcc988800001ae
def unflatten(flat_array, depth, direction=True):
    for _ in range(depth):
        new_array = []
        i = 0 if direction else len(flat_array) - 1
        while direction and i < len(flat_array) or not direction and i >= 0:
            new_e = None
            shift = None
            if not isinstance(flat_array[i], list):
                r = flat_array[i] % (len(flat_array) - i if direction else i + 1)
                if r < 3:
                    new_e = flat_array[i]
                    shift = 1
                else:
                    new_e = flat_array[i:i + r] if direction else flat_array[i - r + 1:i + 1]
                    shift = r
            else:
                new_e = unflatten(flat_array[i], 1, direction)
                shift = 1
            if direction:
                new_array.append(new_e)
                i += shift
            else:
                new_array = [new_e] + new_array
                i -= shift
        flat_array = new_array
        direction = not direction
    return flat_array
                