# https://www.codewars.com/kata/569d488d61b812a0f7000015
def data_reverse(data):
    return [bit for i in range(len(data), 0, -8) for bit in data[i - 8:i]]