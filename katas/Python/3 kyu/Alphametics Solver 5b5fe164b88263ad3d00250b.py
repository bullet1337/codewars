# https://www.codewars.com/kata/5b5fe164b88263ad3d00250b
import itertools
import re
from collections import Counter


def alphametics(puzzle):
    words = re.findall(r'[A-Z]+', puzzle)

    def helper(letters, i=0, part_s=0):
        if any(len(w) > 1 and letters.get(w[0]) == 0 for w in words):
            return

        last_letters = Counter(w[~i] for w in words[:-1] if i < len(w))
        if not last_letters and i >= len(words[-1]):
            return letters if part_s == 0 else None

        new_letters = [l for l in last_letters if l not in letters]
        used_digits = set(letters.values())
        lw_letter = words[-1][~i]
        if new_letters:
            for comb in itertools.permutations((d for d in range(10) if d not in letters.values()), len(new_letters)):
                l_d = dict(zip(new_letters, comb))
                s = part_s + sum(c * letters.get(l, l_d.get(l)) for l, c in last_letters.items())
                lw_letter_digit = letters.get(lw_letter, l_d.get(lw_letter))
                if lw_letter_digit is not None:
                    if lw_letter_digit != s % 10:
                        continue
                elif s % 10 in comb or s % 10 in used_digits:
                    continue
                else:
                    letters[lw_letter] = s % 10

                letters.update(l_d)
                x = helper(letters, i + 1, s // 10)
                if x:
                    return x
                for l in l_d:
                    letters.pop(l)
                if lw_letter_digit is None:
                    letters.pop(lw_letter)
        else:
            s = part_s + sum(c * letters[l] for l, c in last_letters.items())
            lw_letter_digit = letters.get(lw_letter)
            if lw_letter_digit is not None:
                if lw_letter_digit != s % 10:
                    return
            elif s % 10 in used_digits:
                return
            else:
                letters[lw_letter] = s % 10

            x = helper(letters, i + 1, s // 10)
            if x:
                return x
            if lw_letter_digit is None:
                letters.pop(lw_letter)

    x = helper({})
    return ''.join(str(x.get(l, l)) for l in puzzle)