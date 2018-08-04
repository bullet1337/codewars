# https://www.codewars.com/kata/574bd867d277832448000adf
import re


def is_audio(file_name):
    return bool(re.fullmatch('[a-zA-Z]+\.(mp3|[af]lac|aac)', file_name))

def is_img(file_name):
    return bool(re.fullmatch('[a-zA-Z]+\.(jpe?g|png|bmp|gif)', file_name))