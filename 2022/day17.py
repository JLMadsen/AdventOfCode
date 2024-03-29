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

def solve(content, n_rocks, grid = set()):
    global width; width = 7
    highest_point = 0
    direction_idx = 0

    for n in range(n_rocks):
        rock = set()
        for y, row in enumerate(SHAPES[n % len(SHAPES)][::-1]):
            for x, char in enumerate(row):
                if char == '#':
                    rock.add((x + 2, y + highest_point + 3))

        if (highest_point > 0 and
            n % len(SHAPES) == 0 and
            direction_idx == 0 ):
            print('LOOP')

        while True:
            # print_tetris(grid | rock)
            direction = content[direction_idx % len(content)]
            direction_idx += 1

            if direction == '>':
                for (x, y) in rock:
                    if (x+1, y) in grid or x+1 >= width:
                        break
                else:
                    rock = set([(x+1,y) for (x,y) in rock])

            if direction == '<':
                for (x, y) in rock:
                    if (x-1, y) in grid or x-1 < 0:
                        break
                else:
                    rock = set([(x-1,y) for (x,y) in rock])

            if not any( ((x, y-1) in grid or ((y-1) < 0)) for (x,y) in rock ):
                rock = set([(x, y-1) for (x, y) in rock])
            else:
                grid |= rock
                for (x, y) in rock:
                    highest_point = max(highest_point, y + 1)
                break

    print_tetris(grid)
    print(highest_point)

def part2(content):
    pass

if __name__ == "__main__":
    with open('input/day17.txt') as f:
        content = f.read().splitlines()[0]
        solve(content, 2022) # 3055
        # solve(content, 1000000000000)