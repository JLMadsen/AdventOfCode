from collections import defaultdict

def adjacent(x, y):
    return [(x    , y    ), (x    , y    ),
            (x + 1, y    ), (x - 1, y    ),
            (x    , y + 1), (x    , y - 1)]

directions = {
    '^': (0, -1),
    'v': (0,  1),
    '<': (-1, 0),
    '>': ( 1, 0)}

def print_blizzard():
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            point = (x, y)
            char = '.'
            if point in walls: char ='#'
            if point in elves: char = 'P'
            if point == goal:  char = 'E'
            if point in tornado_set:
                dirs = tornado_dir[point]
                char = dirs[0] if len(dirs) < 2 else len(dirs)
            print(char, end='')
        print()
    print()

def solve(content, steps = 0):
    global walls, start, goal, tornado_set, tornado_dir, xmax, ymax, elves
    walls = set()
    goal = start = (0, 0)

    tornado_set = set()
    tornado_dir = defaultdict(lambda: []) # (x, y): ['<','V']

    ymax = xmax = 0
    for y, line in enumerate(content):
        ymax = max(ymax, y)
        for x, value in enumerate(line):
            xmax = max(xmax, x)
            point = (x, y)

            if y == 0 and value == '.':
                start = point

            if y == (len(content) -1) and value == '.':
                goal = point

            if value == '#':
                walls.add(point)

            if value in '<v>^':
                tornado_set.add(point)
                tornado_dir[point].append(value)

    elves = set([start])

    def step_blizzard():
        global tornado_dir, tornado_set
        new_tornado_set = set()
        new_tornado_dir = defaultdict(lambda: [])

        for tornado in tornado_set:
            for dir in tornado_dir[tornado]:

                delta = directions[dir]

                dx = tornado[0] + delta[0]
                dy = tornado[1] + delta[1]

                if   dx == 0:    dx = xmax - 1
                elif dx >= xmax: dx = 1
                elif dy == 0:    dy = ymax - 1
                elif dy >= ymax: dy = 1

                delta_tornado = (dx, dy)
                
                new_tornado_set.add(delta_tornado)
                new_tornado_dir[delta_tornado].append(dir)
        
        tornado_set = new_tornado_set
        tornado_dir = new_tornado_dir

    def step_elves():
        global elves
        new_elves = set([start])

        for elf in elves:
            for delta_elf in adjacent(*elf):
                if delta_elf == goal: return True
                if (delta_elf not in walls and 
                    delta_elf not in tornado_set):
                    new_elves.add(delta_elf)
        
        elves = new_elves
        return False

    reached_goal = False
    minute = 0

    while not reached_goal:
        # print_blizzard()
        step_blizzard()
        reached_goal = step_elves()
        minute += 1

    print(minute)
    # 153 < 

ex = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

if __name__ == "__main__":
    with open('input/day24.txt') as f:
        content = f.read().splitlines()
        content = ex.splitlines()
        solve(content)