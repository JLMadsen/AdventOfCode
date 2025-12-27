
import math
import re
from collections import defaultdict
nth = lambda arr, n: [r[n] for r in arr]

def part1(content):
    value = 0
    coords = []

    for line in content:
        coords.append(tuple(map(int, line.split(','))))

    for i, a in enumerate(coords[:-1]):
        for b in coords[i+1:]:
            x1, y1 = a
            x2, y2 = b
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            value = max(area, value)

    print(value)

def part2(content):
    pass

testdata = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = f.read().splitlines()
        test = testdata.splitlines()
        part1(content) # 4737096935
        part1(test)
        # part2(content)
        # part2(test)
