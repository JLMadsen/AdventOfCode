from collections import defaultdict

directions = {
    '^': (0, -1),
    'v': (0,  1),
    '<': (-1, 0),
    '>': ( 1, 0)
}

dir_to_emoji = lambda d: '🔼🔽⏩⏪'['^v><'.index(d)]

nth = lambda arr, n: [*zip(*arr)][n-1]
def print_blizzard():
    for y in range(ymax):
        for x in range(xmax):
            point = (x, y)
            char = '⬛'
            if point in walls:
                char = '⬜'
            if point == player:
                char = '👽'
            if point == goal:
                char = '🥅'
            if point in tornado_set:
                dirs = tornado_dir[point]
                char = dir_to_emoji(dirs[0]) if len(dirs) == 1 else str(len(dirs)).rjust(2)
            print(char, end='')
        print()

def solve(content, steps = 0):
    global walls, player, goal, tornado_set, tornado_dir, xmax, ymax, players
    walls = set()
    players = set()
    player = (0, 0)
    goal = (0, 0)

    tornado_set = set()
    tornado_dir = defaultdict(lambda: []) # (x, y): ['<','V']

    ymax = xmax = 0
    for y, line in enumerate(content):
        ymax = max(ymax, y + 1)
        for x, value in enumerate(line):
            xmax = max(xmax, x + 1)
            point = (x, y)

            if y == 0 and value == '.':
                player = point

            if y == (len(content) -1) and value == '.':
                goal = point

            if value == '#':
                walls.add(point)

            if value in '<v>^':
                tornado_set.add(point)
                tornado_dir[point].append(value)

    print(xmax, ymax)

    # print(player, goal)
    # print_blizzard()

    # state
    #   minute
    #   position

    def step_blizzard():
        global tornado_dir, tornado_set

        new_tornado_set = set()
        new_tornado_dir = defaultdict(lambda: [])

        for tornado in tornado_set:
            for dir in tornado_dir[tornado]:

                delta = directions[dir]

                dx = tornado[0] + delta[0]
                dy = tornado[1] + delta[1]

                if   dx == 0:        dx = xmax - 2
                elif dx >= xmax - 1: dx = 1
                elif dy == 0:        dy = ymax - 2
                elif dy >= ymax - 1: dy = 1

                delta_tornado = (dx, dy)
                
                new_tornado_set.add(delta_tornado)
                new_tornado_dir[delta_tornado].append(dir)
        
        tornado_set = new_tornado_set
        tornado_dir = new_tornado_dir

    print_blizzard()

    # state = [(player, 0)]

    reached_goal = False
    while not reached_goal:
        step_blizzard()
        # step_blizzard()
        # step_blizzard()
        print_blizzard()

        exit()




    

                


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