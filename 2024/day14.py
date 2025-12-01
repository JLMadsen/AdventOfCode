
import math
import re
from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

def part1(content):
    value = 0
    for line in content:
        print(line)

    print(value)

def part2(content):
    pass

if __name__ == "__main__":
    with open('input/day14.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
