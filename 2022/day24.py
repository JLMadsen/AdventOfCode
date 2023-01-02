from collections import defaultdict

def adjacent(x, y): return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
directions = {'^': (0, -1), 'v': (0,  1),'<': (-1, 0), '>': ( 1, 0)}

def print_blizzard():
    [[print((((point := (x, y)) in walls and '#') or (point in elves and 'P') or (point == goal  and 'E') or (point in tornado and (dirs[0] if len((dirs := tornado[point])) < 2 else len(dirs))) or '.'), end='') if x<xmax+1 else print() for x in range(xmax + 2)]for y in range(ymax + 1)]

def solve(content, pt2 = False, minute = 0):
    global walls, goal, tornado, xmax, ymax, elves
    walls = set()
    goal = start = (0, 0)
    tornado = defaultdict(lambda: []) # (x, y): ['<','V']

    ymax, xmax = (len(content)-1) , (len(content[0])-1)
    for y, line in enumerate(content):
        for x, value in enumerate(line):
            point = (x, y)

            if y == 0    and value == '.': start = point
            if y == ymax and value == '.': goal = point
            if value == '#':               walls.add(point)
            if value in directions:        tornado[point].append(value)

    def step_blizzard():
        global tornado
        new_tornado = defaultdict(lambda: [])

        for point, dirs in tornado.items():
            for dir in dirs:
                delta = directions[dir]
                dx = point[0] + delta[0]
                dy = point[1] + delta[1]

                if   dx == 0:    dx = xmax - 1
                elif dx >= xmax: dx = 1
                elif dy == 0:    dy = ymax - 1
                elif dy >= ymax: dy = 1

                new_tornado[(dx, dy)].append(dir)
        tornado = new_tornado

    def step_elves():
        global elves
        new_elves = set([start])
        obstacles = walls | tornado.keys()

        for elf in elves:
            for next_elf in adjacent(*elf) + [elf]:
                if next_elf == goal: return True

                if (next_elf not in obstacles and 
                    xmax >= next_elf[0] >= 0  and 
                    ymax >= next_elf[1] >= 0):

                    new_elves.add(next_elf)
        elves = new_elves
        return False

    for d in range(1+2*pt2):
        elves = set([start])

        while True:
            minute += 1
            step_blizzard()
            if step_elves(): break

        start, goal = goal, start

    # print_blizzard()
    print(minute)

if __name__ == "__main__":
    with open('input/day24.txt') as f:
        content = f.read().splitlines()
        solve(content) # 266
        solve(content, True) # 853