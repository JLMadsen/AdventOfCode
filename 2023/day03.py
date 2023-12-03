import math
from collections import defaultdict

def solve(content, total=0, ratios=0):
    buffer      = ''
    has_symbol  = False
    gear_pos    = None
    gears       = defaultdict(lambda: [])

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
                            if adj == '*':
                                gear_pos=(i+di,dj+j)
                        except: pass

            else:
                if has_symbol: total += int(buffer)
                if gear_pos:   gears[gear_pos].append(int(buffer))
                buffer = ''
                has_symbol = False
                gear_pos = None
    
    for n in gears.values():
        if len(n) > 1:
            ratios += math.prod(n)

    print(total)
    print(ratios)

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        solve(content)