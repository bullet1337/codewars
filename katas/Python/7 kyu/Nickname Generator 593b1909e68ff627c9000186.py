# https://www.codewars.com/kata/593b1909e68ff627c9000186
def nickname_generator(name):
    return name[:3 + (name[2].lower() in 'aioue')] if len(name) > 3 else 'Error: Name too short'