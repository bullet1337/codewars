# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
def sort_array(source_array):
    indices = [i for i, e in enumerate(source_array) if e % 2 != 0]
    sorted_odd = sorted(source_array[i] for i in indices)
    for i, e in zip(indices, sorted_odd):
        source_array[i] = e
    return source_array