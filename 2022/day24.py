from collections import defaultdict

def adjacent(x, y):
    return [(x + 1, y    ), (x - 1, y    ),
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
            if point in walls: char = '#'
            if point in elves: char = 'P'
            if point == goal:  char = 'E'
            if point in tornado_set:
                dirs = tornado_dir[point]
                char = dirs[0] if len(dirs) < 2 else len(dirs)
            print(char, end='')
        print()
    print()

def solve(content, pt2 = False, minute = 0):
    global walls, start, goal, tornado_set, tornado_dir, xmax, ymax, elves
    walls = set()
    goal = start = (0, 0)
    tornado_set = set()
    tornado_dir = defaultdict(lambda: []) # (x, y): ['<','V']

    ymax, xmax = (len(content)-1) , (len(content[0])-1)
    for y, line in enumerate(content):
        for x, value in enumerate(line):
            point = (x, y)

            if y == 0 and value == '.':    start = point
            if y == ymax and value == '.': goal = point
            if value == '#':               walls.add(point)
            if value in '<v>^':
                tornado_set.add(point)
                tornado_dir[point].append(value)

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

                new_tornado_set.add((dx, dy))
                new_tornado_dir[(dx, dy)].append(dir)

        tornado_set = new_tornado_set
        tornado_dir = new_tornado_dir

    def step_elves():
        global elves
        new_elves = set([start])
        obstacles = walls | tornado_set

        for elf in elves:
            for next_elf in adjacent(*elf) + [elf]:
                if next_elf == goal: return True

                if (next_elf not in obstacles and 
                    xmax >= next_elf[0] >= 0  and 
                    ymax >= next_elf[1] >= 0):

                    new_elves.add(next_elf)
        elves = new_elves
        return False

    for d in range(1 if not pt2 else 3):
        elves = set([start])
        reached_goal = False

        while not reached_goal:
            step_blizzard()
            reached_goal = step_elves()
            minute += 1

        start, goal = [start, goal][::(1-(2*pt2))]

    print(minute)

if __name__ == "__main__":
    with open('input/day24.txt') as f:
        content = f.read().splitlines()
        solve(content) # 266
        solve(content, True) # 853