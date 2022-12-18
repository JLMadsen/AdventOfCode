
import math
import re
from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

SHAPES = [
    ["####"], 

    [".#.",
     "###",
     ".#."],

    ["..#",
     "..#",
     "###"],

    ["#",
     "#",
     "#",
     "#"],

    ["##",
     "##"],
]

def print_tetris(grid):
    for y in range(10, -1, -1):
        print('|', end='')
        for x in range(width ):
            print('⬜' if (x,y) in grid else '◾', end='')
        print('|')
    print('+'+('--'*7)+'+')

def part1(content):
    
    rock_id = 0
    
    grid = set()
    global width; width = 7
    highest_point = 0
    pieces = 2021
    direction_idx = 0

    # for direction in content:
    for n in range(pieces + 1):
        rock = set()
        points = SHAPES[n % len(SHAPES)]
        # print('Rock', n)
        for y, row in enumerate(points[::-1]):
            for x, char in enumerate(row):
                if char == '#':
                    rock.add((x + 2, y + highest_point + 3))

        # print_tetris(grid | rock)

        while True:
            # print_tetris(grid | rock)
            # print()

            direction = content[direction_idx % len(content)]
            direction_idx += 1

            if direction == '>':
                for (x, y) in rock:
                    dx = x + 1
                    if (dx, y) in grid: break
                    if dx >= width:     break
                else:
                    rock = set([(x+1,y) for (x,y) in rock])

            elif direction == '<':
                for (x, y) in rock:
                    dx = x - 1
                    if (dx, y) in grid: break
                    if dx < 0:          break
                else:
                    rock = set([(x-1,y) for (x,y) in rock])

            if not any( ((x, y-1) in grid or 
                        ((y-1) < 0)) for (x,y) in rock ):

                rock = set([(x, y-1) for (x, y) in rock])
            else:
                # print(rock, direction)
                grid |= rock

                for (x, y) in rock:
                    highest_point = max(highest_point, y + 1)

                # print_tetris(grid)
                # exit()
                break

            
    print(highest_point)

def part2(content):
    pass

ex = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

if __name__ == "__main__":
    with open('input/day17.txt') as f:
        content = f.read().splitlines()[0]
        # content = ex
        part1(content)
        part2(content)
