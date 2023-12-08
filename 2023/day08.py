
import math
import re
from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

def part1(content, value=0, ways={}):
    lr = content.pop(0)
    position = 'AAA'

    for line in content[1:]:
        start, _, left, right = line.split()
        ways[start] = [left[1:-1], right[:-1]]

    while position != 'ZZZ':
        direction = lr[value % len(lr)]
        value += 1
        position = ways[position][direction == 'R']

    print(value)

def part2(content, value=0, ways={}):
    lr = content.pop(0)
    ghosts = []
    
    for line in content[1:]:
        start, _, left, right = line.split()
        ways[start] = [left[1:-1], right[:-1]]
        if start[-1] == 'A':
            ghosts.append(start)

    steps = []

    while len(ghosts) > 0:
        direction = lr[value % len(lr)]
        value += 1
        new_ghosts = []
        for node in ghosts:
            new = ways[node][direction == 'R']
            if new[-1] != 'Z':
                new_ghosts.append(new)
            else:
                steps.append(value)
        ghosts = new_ghosts

    print(math.lcm(*steps))

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().splitlines()
        part1([*content]) # 17287
        part2([*content]) # 18625484023687