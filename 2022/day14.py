nth = lambda arr, n: [*zip(*arr)][n-1]

def print_waterfall(walls):
    xmin, xmax = min(nth([*walls], 1)), max(nth([*walls], 1)) + 1
    ymin, ymax = min(nth([*walls], 0)), max(nth([*walls], 0))

    ymin = 0
    ymax += 1

    print(xmin, xmax)
    print(ymin, ymax)

    print('_'*(ymax-ymin+5))
    print(' ', ''.join([str(i)[-1] for i in range(xmin, xmax)]))

    for dy in range(ymin, ymax):
        print(f'{dy} ', end='')
        for dx in range(xmin, xmax):
            print('#' if (dx, dy) in walls else '.', end='')
        print()

    print('_'*(ymax-ymin+5))


def part1(content):

    walls = set()
    value = 0


    for line in content:
        steps = [*map(lambda n: [*map(int, n.split(','))], line.split(' -> '))]
        print(steps)

        for i in range(len(steps) - 1):
            (ax, ay), (bx, by) = steps[i], steps[i+1]
            # print(ax, ay, '->', bx, by)
            # print('diff', abs(ax-bx), abs(ay-by))

            if ax == bx:
                for n in range(abs(ay - by) + 1):
                    dy = ay + (n if ay < by else -n)
                    # print('>',(ax, dy))
                    walls.add((ax, dy))

            if ay == by:
                for n in range(abs(ax - bx) + 1):
                    dx = ax + (n if ax < bx else -n)
                    # print('>',(dx, ay))
                    walls.add((dx, ay))

    print(walls)
    print_waterfall(walls)

    print(value)

def part2(content):
    pass

ex = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

if __name__ == "__main__":
    with open('input/day14.txt') as f:
        content = f.read().splitlines()
        content = ex.splitlines()

        part1(content)
        part2(content)
