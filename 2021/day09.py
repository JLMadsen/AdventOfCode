def get_adjacent(grid, i, j, pos=False):
    adjacent = []

    for neighbor in [(1,0), (0,1), (-1,0),(0,-1)]:
        x, y = j + neighbor[0], i + neighbor[1]
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) :
            continue
        adjacent.append(grid[y][x] if not pos else [y, x])
    
    return adjacent

low_points = []

def calc_risk(grid):
    global low_points
    risk = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if all([value < a for a in get_adjacent(grid, i, j)]):
                risk += value + 1
                low_points.append([i, j])
    return risk

def calc_basin(grid):
    global low_points
    basins = []

    for point in low_points:

        if any([point in basin for basin in basins]):
            continue

        # ​breadth-first search 
        visited = [point]
        queue = [point]

        while queue:
            y1, x1 = queue.pop(0)

            for y2, x2 in get_adjacent(grid, y1, x1, True):

                if [y2, x2] not in visited and grid[y2][x2] != 9:
                    visited.append([y2, x2])
                    queue.append([y2, x2])

        basins.append(visited)
    
    basins = sorted(basins, key=len)
    return len(basins[-1]) * len(basins[-2]) * len(basins[-3])

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = [*map(lambda x: [*map(lambda y: int(y), [c for c in x])] , f.read().split('\n')[:-1])]

        print(calc_risk(content)) # 436
        print(calc_basin(content)) # 1317792