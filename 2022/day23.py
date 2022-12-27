
import math
import re
from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

def adjacent(x, y):
    return [(x + 1, y),     (x, y + 1),
            (x - 1, y),     (x, y - 1),
            (x + 1, y + 1), (x - 1, y - 1),
            (x + 1, y - 1), (x - 1, y + 1)]

def part1(content):
    value = 0
    elves = set()

    for y, line in enumerate(content):
        for x, value in enumerate(line):
            if value == '#':
                elves.add((x,y))

    

    print(elves)

    print(value)

def part2(content):
    pass

if __name__ == "__main__":
    with open('input/day23.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
