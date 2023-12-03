import math
from collections import defaultdict

def part1(content, value = 0):
    

    nums = []
    buffer = ''
    has_symbol = False
    for i, line in enumerate(content):
        for j, char in enumerate(line):
            if char.isdigit():
                buffer += char
                for di in [-1,0,1]:
                    for dj in [-1,0,1]:
                        try:
                            adj = content[i+di][dj+j]
                            if not adj.isdigit() and adj != '.':
                                has_symbol = True
                        except: pass
            elif not char.isdigit():
                if has_symbol:
                    nums.append(int(buffer))
                buffer = ''
                has_symbol = False
    print(sum(nums))

def part2(content):
    value = 0

    nums = []
    buffer = ''
    has_symbol = False
    gear_pos = None
    gears = defaultdict(lambda: [])
    for i, line in enumerate(content):
        for j, char in enumerate(line):
            if char.isdigit():
                buffer += char
                for di in [-1,0,1]:
                    for dj in [-1,0,1]:
                        try:
                            adj = content[i+di][dj+j]
                            if adj == '*':
                                has_symbol = True
                                gear_pos=(i+di,dj+j)
                        except: pass
            elif not char.isdigit():
                if has_symbol:
                    gears[gear_pos].append(int(buffer))
                    nums.append(int(buffer))
                buffer = ''
                has_symbol = False
    
    for n in gears.values():
        if len(n) > 1:
            value += math.prod(n)

    print(value)

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        part1(content) # 507214
        part2(content) # 72553319
