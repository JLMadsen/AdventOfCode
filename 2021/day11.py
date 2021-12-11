def flash(grid, y, x, flashed):
    flashes = 0
    
    if grid[y][x] > 9 and (y, x) not in flashed:
        flashes += 1
        flashed.add((y, x))

        for dy in [1, 0, -1]:
            for dx in [1, 0, -1]:

                my, mx = dy + y, dx + x
                if ( my < 0 or 
                     mx < 0 or 
                     my >= len(grid) or 
                     mx >= len(grid[0]) or (
                     dy == 0 and dx == 0 )):
                    continue

                grid[my][mx] += 1
                flashes += flash(grid, my, mx, flashed)

    return flashes

def simulate(grid, steps = 100, sync = False):
    flashes = 0
    h, w = len(grid), len(grid[0])

    for step in range(steps if steps > 0 else int(9E10)):

        if sync:
            if sum( [ sum(row) for row in grid ] ) == 0:
                return step

        flashed = set()

        for y in range(h):
            for x in range(w):
                grid[y][x] += 1
                flashes += flash(grid, y, x, flashed)
        
        for y in range(h):
            for x in range(w):
                grid[y][x] *= 0 if grid[y][x] > 9 else 1

    return flashes 

if __name__ == "__main__":
    with open('input/day11.txt') as f:
        content = f.read().split('\n')[:-1]
        grid = [[int(value) for value in line] for line in content]

        print(simulate([row[:] for row in grid])) # 1725
        print(simulate(grid, -1, True)) # 308