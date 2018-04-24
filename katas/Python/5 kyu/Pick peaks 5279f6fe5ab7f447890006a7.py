# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7
def pick_peaks(arr):
    print(arr)
    pos = []
    peaks = []

    if len(arr) < 2:
        return {'pos': pos, 'peaks': peaks}

    asc = arr[1] > arr[0]
    plateu_start = None
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            if plateu_start is None:
                plateu_start = i - 1
        elif asc and arr[i] < arr[i - 1] or not asc and arr[i] > arr[i - 1]:
            if asc:
                pos.append(plateu_start or i - 1)
                peaks.append(arr[i - 1])
            plateu_start = None
            asc = not asc
        else:
            plateu_start = None

    return {'pos': pos, 'peaks': peaks}