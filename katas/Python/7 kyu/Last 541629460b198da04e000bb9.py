# https://www.codewars.com/kata/541629460b198da04e000bb9
def last(*args):
  return args[-1][-1] if isinstance(args[-1], (list, str)) else args[-1]