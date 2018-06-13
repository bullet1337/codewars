# https://www.codewars.com/kata/59c5d0b0a25c8c99ca000237
def line(grid):
    total = 0
    x = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ' ':
                total += 1
                if grid[i][j] == 'X':
                    x.append((i, j))
    if len(x) != 2:
        return False
        
    moves = {'+': [(0, 1), (1, 0), (0, -1), (-1, 0)], '-': [(0, 1), (0, -1)], '|': [(1, 0), (-1, 0)]}
    moves['X'] = moves['+']

    for start, finish in [x, x[::-1]]:
        good = 0
        stack = [(start[0], start[1], {}, None)]
        while stack:
            x, y, visited, last_move = stack.pop()
            if (x, y) == finish:
                if len(visited) == total - 1:
                    return True
                continue
            
            possibles = []
            for move in moves[grid[x][y]]:
                x_new, y_new = x + move[0], y + move[1]
                if 0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]) and grid[x_new][y_new] != ' ' and (x_new, y_new) not in visited \
                        and grid[x_new][y_new] in moves \
                        and (move[0] == 0 and grid[x_new][y_new] != '|' or move[0] != 0 and grid[x_new][y_new] != '-') \
                        and (grid[x][y] != '+' or last_move[0] != move[0]):
                    visited = set(visited)
                    visited.add((x, y))
                    possibles.append((x_new, y_new, visited, move))
            if len(possibles) == 1:
                stack.append(possibles[0])
    return False