# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111
def triangle(row):
    colors = set('RGB')
    while len(row) > 1:
        row = ''.join([row[i] if row[i] == row[i + 1] else (colors - {row[i], row[i + 1]}).pop()
                       for i, c in enumerate(row[:-1])])
    return row