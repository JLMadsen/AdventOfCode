def patrol(grid):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    way = dirs[-1]
    visited = set()
    crashed = set()
    x, y = 0, 0

    for i, line in enumerate(grid):
        if '^' in line:
            y = i
            x = line.index('^')
            break
    visited.add((x, y))

    while (x >= 0 and x <= len(grid[0]) and y >= 0 and y <= len(grid)):
        try:
            while 1:
                dx, dy = way
                infront = grid[y + dy][x + dx]
                if infront == '#':
                    crash = (x, y, dx, dy)
                    if crash in crashed:
                        return 0
                    crashed.add(crash)
                    break
                
                x += dx
                y += dy

                visited.add((x, y))

            way = dirs[ dirs.index(way) - 1 ]
        except:
            break

    return len(visited)

def part1(content):
    print(patrol(content))

def part2(content):
    loops = 0
    for i in range(len(content)):
        for j in range(len(content[0])):
            if content[i][j] == '#':
                continue
            
            new_grid = [[c for c in line] for line in content]
            new_grid[i][j] = '#'

            if not patrol(new_grid):
                loops += 1

    print(loops)

if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
