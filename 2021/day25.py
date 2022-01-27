import sys

def print_grid(grid):
    for r in grid:
        print(''.join(r))
    print()

def simulate(grid):
    
    print('grid_size', len(grid), 'x', len(grid[0]))
    print('initial state')
    print_grid(grid)

    for step in range(1, sys.maxsize):
        
        new_grid = [row[:] for row in grid]
        did_step = False

        for mod, char in [[(0, 1), '>'], [(1, 0), 'v']]:
            for y1, row in enumerate(grid):
                for x1, val in enumerate(row):
                    if char == val:

                        y2 = (y1 + mod[0]) % len(grid)
                        x2 = (x1 + mod[1]) % len(grid[0])

                        if grid[y2][x2] == '.':

                            new_grid[y1][x1] = '.'
                            new_grid[y2][x2] = char
                            did_step = True

            grid = new_grid
        print('step', step)
        print_grid(grid)

        if step > 3:
            print('stopping @', step)
            return

        if not did_step:
            print(step)
            return


test = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

test = """...>...
.......
......>
v.....>
......>
.......
..vvv.."""

#test = "..>>>>...."

if __name__ == "__main__":
    with open('input/day25.txt') as f:
        content = test.split('\n') # f.read().split('\n')[:-1]
        
        content = [[*line] for line in content]

        simulate(content)