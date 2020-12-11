import re
from collections import defaultdict

def lights(data):

    grid = defaultdict(lambda: defaultdict(lambda: 0))

    for instruction in data:

        s_row, s_col, e_row, e_col = [*map(int, re.findall(r'\d+', instruction))]

        for r in range(s_row, e_row+1):
            for c in range(s_col, e_col+1):

                if 'toggle' in instruction:
                    grid[r][c] = 1 if not grid[r][c] else 0
                elif 'on' in instruction:
                    grid[r][c] = 1
                elif 'off' in instruction:
                    grid[r][c] = 0

    count = 0
    for row in grid.values():
        for col in row.values():
            count += col
    print(count)

def lights_brightness(data):

    grid = defaultdict(lambda: defaultdict(lambda: 0))

    for instruction in data:

        s_row, s_col, e_row, e_col = [*map(int, re.findall(r'\d+', instruction))]

        for r in range(s_row, e_row+1):
            for c in range(s_col, e_col+1):

                if 'toggle' in instruction:
                    grid[r][c] += 2
                elif 'on' in instruction:
                    grid[r][c] += 1 
                elif 'off' in instruction:
                    grid[r][c] -= 1 if grid[r][c] > 0 else 0

    count = 0
    for row in grid.values():
        for col in row.values():
            count += col
    print(count)

if __name__ == "__main__":
    with open('2015/input/day06.txt') as f:

        data = f.read().splitlines()

        lights(data)            # 377891
        lights_brightness(data) # 14110788
