# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa
def is_merge(s, part1, part2, i=0, j=0):
    for k, c in enumerate(s):
        if i < len(part1) and part1[i] == c:
            if j < len(part2) and part2[j] == c:
                return is_merge(s[k + 1:], part1, part2, i + 1, j) or is_merge(s[k + 1:], part1, part2, i, j + 1)
            else:
                i += 1
        elif j < len(part2) and part2[j] == c:
            j += 1
        else:
            return False
    return i == len(part1) and j == len(part2)