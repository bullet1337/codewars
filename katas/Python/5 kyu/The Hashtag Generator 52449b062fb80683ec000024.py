# https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s):
    if not s:
        return False

    s = '#' + s.title().replace(' ', '')
    return s if len(s) <= 140 else False