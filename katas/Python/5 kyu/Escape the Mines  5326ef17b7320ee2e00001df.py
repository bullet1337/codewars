# https://www.codewars.com/kata/5326ef17b7320ee2e00001df
opposites = {
    'up': 'down',
    'down': 'up',
    'left': 'right',
    'right': 'left'
}

def solve(map, miner, exit, path=[]):
    if not(0 <= miner['x'] < len(map) and 0 <= miner['y'] < len(map[0])) \
        or not map[miner['x']][miner['y']] \
        or len(path) > 1 and path[-2] == opposites[path[-1]]:
        return []
    if miner['x'] == exit['x'] and miner['y'] == exit['y']:
        return path
    
    return solve(map, {'x': miner['x'] - 1, 'y': miner['y']}, exit, path + ['left']) \
        or solve(map, {'x': miner['x'] + 1, 'y': miner['y']}, exit, path + ['right']) \
        or solve(map, {'x': miner['x'], 'y': miner['y'] - 1}, exit, path + ['up']) \
        or solve(map, {'x': miner['x'], 'y': miner['y'] + 1}, exit, path + ['down'])
        