nth = lambda arr, n: [*zip(*arr)][n-1]
xmin = xmax = ymin = ymax = 0

def print_waterfall(walls, sands):
    print(' ', ' '.join([str(i)[-1] for i in range(xmin, xmax)]))
    for dy in range(ymin, ymax):
        print(f'{dy}'.rjust(4), end='')
        for dx in range(xmin, xmax):
            print('⬜' if (dx, dy) in walls else (
                  '💛' if (dx, dy) in sands else 
                  '⬛'), end='')
        print()

def solve(content, pt2 = False, walls = set(), sands = set()):
    for line in content:
        steps = [*map(lambda n: 
                [*map(int, n.split(','))], 
                line.split(' -> '))]

        for (ax, ay), (bx, by) in zip(steps, steps[1:]):
            if ax == bx:
                for n in range(abs(ay - by) + 1):
                    dy = ay + (n if ay < by else -n)
                    walls.add((ax, dy))

            if ay == by:
                for n in range(abs(ax - bx) + 1):
                    dx = ax + (n if ax < bx else -n)
                    walls.add((dx, ay))

    global xmin, xmax, ymin, ymax
    xmin, xmax = min(nth([*walls], 1)), max(nth([*walls], 1)) + 1
    ymin, ymax = 0,                     max(nth([*walls], 0)) + 1

    done = False
    while not done:
        sand, resting = (500, 0), False

        while not resting:
            down       = (sand[0],     sand[1] + 1)
            down_left  = (sand[0] - 1, sand[1] + 1)
            down_right = (sand[0] + 1, sand[1] + 1)

            for next_pos in [down, down_left, down_right]:
                if (next_pos not in walls and 
                    next_pos not in sands and 
                   (next_pos[1] < ymax + 1 if pt2 else 1)):

                    sand = next_pos
                    break
            else:
                done = pt2 and sand == (500, 0)
                sands.add(sand)
                resting = True

            if sand[1] > ymax and not pt2:
                done = resting = True
  
    # if not pt2: print_waterfall(walls, sands)
    print(len(sands))

if __name__ == "__main__":
    with open('input/day14.txt') as f:
        content = f.read().splitlines()
        solve(content) # 578
        solve(content, True) # 24377