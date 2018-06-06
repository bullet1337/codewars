# https://www.codewars.com/kata/5993c1d917bc97d05d000068
from collections import defaultdict


def regex_divisible_by(n):
    states = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for i in range(n):
        states[i][True][i * 2 % n].append('0')
        states[i * 2 % n][False][i].append('0')

        states[i][True][(i * 2 + 1) % n].append('1')
        states[(i * 2 + 1) % n][False][i].append('1')

    for i in range(n, -1, -1):
        star = ''
        if i in states[i][True]:
            star = '(?:{})*'.format('|'.join(states[i][True][i]))
            states[i][True].pop(i)
            states[i][False].pop(i)

        for from_state, from_labels in states[i][False].items():
            from_labels = ('(?:{})' if len(from_labels) > 1 else '{}').format('|'.join(from_labels))
            for to_state, to_labels in states[i][True].items():
                new_label = from_labels + star + ('(?:{})' if len(to_labels) > 1 else '{}').format('|'.join(to_labels))
                states[from_state][True][to_state].append(new_label)
                states[to_state][False][from_state].append(new_label)
        for from_state in states[i][False]:
            states[from_state][True].pop(i)
        for to_state in states[i][True]:
            states[to_state][False].pop(i)
        states.pop(i)
    return '^{}$'.format(star)