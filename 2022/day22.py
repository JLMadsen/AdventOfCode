import re

def print_map():
    for py in range(ymax):
        for px in range(xmax):
            point = (px, py)
            s = ('😀' if point == (x, y) else ('⬜' if point in walls else ('⬛' if point in grid else '  ')))
            print(s, end='')
        print()

""" cube
    ⬛⬜⬜
    ⬛⬜⬛
    ⬜⬜⬛
    ⬜⬛⬛
"""

def solve(content, pt2 = False):
    global grid, walls, xmax, ymax, x, y
    value = 0
    moves = re.findall(r'(\d+|R|L)', content[-1])
    grid = set()
    walls = set()
    xmax = ymax = 0

    for y, line in enumerate(content):
        if not line: break
        for x, value in enumerate(line):
            if value == '.' or value == '#':
                grid.add((x, y))
                xmax, ymax = max(xmax, x), max(ymax, y)
            if value == '#':
                walls.add((x, y))

    x, y = float('inf'), 0
    for (tx, ty) in grid:
        if ty == 0:
            x = min(tx, x)

    side_length = (xmax + 1) // 3

    #         right   down    left     up
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction = 0
    for move in moves:
        if move.isdigit():
            distance = int(move)
            for _ in range(distance):
                dx = x + deltas[direction][0]
                dy = y + deltas[direction][1]

                if (dx, dy) in walls:
                    break

                if not pt2:
                    if (dx, dy) not in grid:
                        point = (0, 0)
                        for n in range(max(ymax, xmax)):
                            ax = x - (n * deltas[direction][0])
                            ay = y - (n * deltas[direction][1]) 
                            if (ax, ay) in grid:
                                point = (ax, ay)
                            else: 
                                break
                        if point not in walls and point in grid:
                            dx, dy = point
                else:
                    pass

                if (dx, dy) in grid:
                    x = dx
                    y = dy
        else:
            direction = (direction + (1 if move == 'R' else -1)) % len(deltas)

    print((1000 * (y+1)) + (4 * (x+1)) + direction )

ex = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

if __name__ == "__main__":
    with open('input/day22.txt') as f:
        content = f.read().splitlines()
        # content = ex.splitlines()

        # solve(content) # 165094
        solve(content, 1)
