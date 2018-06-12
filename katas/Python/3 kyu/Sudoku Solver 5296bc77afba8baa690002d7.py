# https://www.codewars.com/kata/5296bc77afba8baa690002d7
def sudoku(puzzle):
    all = set(range(1, 10))
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [[set() for _ in range(3)] for _ in range(3)]
    zeros = set()
    for i in range(9):
        for j in range(9):
            x = puzzle[i][j]
            if x != 0:
                rows[i].add(x)
                columns[j].add(x)
                boxes[i // 3][j // 3].add(x)
            else:
                zeros.add((i, j))

    while zeros:
        solved = set()
        for i, j in zeros:
            x = all - rows[i] - columns[j] - boxes[i // 3][j // 3]
            if len(x) == 1:
                x = x.pop()
                puzzle[i][j] = x
                rows[i].add(x)
                columns[j].add(x)
                boxes[i // 3][j // 3].add(x)
                solved.add((i, j))
        zeros -= solved
    return puzzle