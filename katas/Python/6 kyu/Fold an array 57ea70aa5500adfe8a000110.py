# https://www.codewars.com/kata/57ea70aa5500adfe8a000110
def fold_array(array, runs):
    for _ in range(runs):
        temp = [array[i] + array[~i] for i in range(len(array) // 2)]
        if len(array) % 2:
            temp.append(array[len(array) // 2])
        array = temp
    return array