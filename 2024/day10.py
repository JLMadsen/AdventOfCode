from collections import defaultdict

def part1(content, trailheads=[], value=0):
    for y, line in enumerate(content):
        for x, char in enumerate(line):
            if char == '0':
                trailheads.append((x, y))

    for start in trailheads:
        visited = set()
        queue = [start]

        while len(queue) > 0:
            x, y = queue.pop(0)
            height = int(content[y][x])

            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                dx += x
                dy += y

                if (0 > dx or dx >= len(content[0]) or
                    0 > dy or dy >= len(content)):
                    continue

                neighbour = content[dy][dx]

                if int(neighbour) - height == 1 and (dx, dy) not in visited:
                    value += neighbour == '9'
                    visited.add((dx, dy))
                    queue.append((dx, dy))

    print(value)

def part2(content):
    trailheads = []
    value = 0

    for y, line in enumerate(content):
        for x, char in enumerate(line):
            if char == '0':
                trailheads.append((x, y))

    for start in trailheads:
        visited = set()

        path = defaultdict(list)
        queue = [start]

        while len(queue) > 0:
            x, y = queue.pop(0)
            height = int(content[y][x])

            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                dx += x
                dy += y

                if (0 > dx or dx >= len(content[0]) or
                    0 > dy or dy >= len(content)):
                    continue

                neighbour = content[dy][dx]

                # for example input
                if neighbour == '.':
                    continue

                if int(neighbour) - height == 1 and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    queue.append((dx, dy))
        
        for x, y in visited:
            if content[y][x] == '9':
                value += 1

    print(value)

t = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

if __name__ == "__main__":
    with open('input/day10.txt') as f:
        content = f.read().splitlines()
        # part1(t.splitlines())
        part1(content)
        part2(content)
