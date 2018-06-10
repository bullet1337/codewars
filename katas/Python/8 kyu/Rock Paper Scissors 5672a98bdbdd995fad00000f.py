# https://www.codewars.com/kata/5672a98bdbdd995fad00000f
win_table = {
    's': {'p': 1, 'r': 2},
    'p': {'s': 2, 'r': 1},
    'r': {'s': 1, 'p': 2}
}


def rps(p1, p2):
    return 'Draw!' if p1 == p2 else 'Player {} won!'.format(win_table[p1[0]][p2[0]])