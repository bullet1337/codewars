# https://www.codewars.com/kata/542ea700734f7daff80007fc
from collections import defaultdict


def processes(start, end, processes):
    transitions = defaultdict(list) 
    for name, source, dest in processes:
        transitions[source].append((name, dest))
        
    stack = [([], start)]
    while stack:
        new_stack = []
        for path, current in stack:
            if current == end:
                return path
            for name, dest in transitions[current]:
                if name not in path:
                    new_stack.append((path + [name], dest))
        stack = new_stack
    return []