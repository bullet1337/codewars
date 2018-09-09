# https://www.codewars.com/kata/565f5825379664a26b00007c
def get_size(w, h, d):
    return [2 * (w * h + w * d + h * d), w * h * d]