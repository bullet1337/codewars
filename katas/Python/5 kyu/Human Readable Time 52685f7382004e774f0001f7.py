# https://www.codewars.com/kata/52685f7382004e774f0001f7
def make_readable(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)