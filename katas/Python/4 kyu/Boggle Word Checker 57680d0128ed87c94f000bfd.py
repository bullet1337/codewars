# https://www.codewars.com/kata/57680d0128ed87c94f000bfd
def find_word(board, word):
    possibles = []
    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            if letter == word[0]:
                possibles.append([(i, j)])

    while possibles:
        p = possibles.pop()
        if len(p) == len(word):
            return True

        for i in range(max(0, p[-1][0] - 1), min(len(board), p[-1][0] + 2)):
            for j in range(max(0, p[-1][1] - 1), min(len(board[0]), p[-1][1] + 2)):
                if (i, j) != p[-1] and (i, j) not in p and board[i][j] == word[len(p)]:
                    possibles.append(p + [(i, j)])

    return False