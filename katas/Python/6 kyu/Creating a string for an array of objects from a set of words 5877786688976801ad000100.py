# https://www.codewars.com/kata/5877786688976801ad000100
def words_to_object(s):
    return '[%s]' % ', '.join(['{name : \'%s\', id : \'%s\'}' % pair for pair in zip(*([iter(s.split())] * 2))])