def get_adjacent(grid, i, j, pos=False):
    return [ grid[y][x] if not pos else [y, x] for a, b in [(1,0), (0,1), (-1,0),(0,-1)] if not ( (x := a + j) < 0 or (y := b + i) < 0 or x >= len(grid[0]) or y >= len(grid) )]

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

        visited, queue = [point], [point]

        while queue:
            y1, x1 = queue.pop(0)
            for y2, x2 in get_adjacent(grid, y1, x1, True):
                if [y2, x2] not in visited and grid[y2][x2] != 9:
                    visited.append([y2, x2])
                    queue.append([y2, x2])

        basins.append(visited)
    
    basins = sorted( [*map(lambda x: len(x), basins)], reverse=True)
    return basins[0] * basins[1] * basins[2]

from PIL import Image
def visualize(grid):
    im= Image.new('RGB', (len(grid), len(grid[0])))
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            color = [25*(10-value)]*3
            im.putpixel((i,j),tuple(color))
    im.save('day09.png')

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = [*map(lambda x: [*map(lambda y: int(y), [c for c in x])] , f.read().split('\n')[:-1])]

        print(calc_risk(content)) # 436
        print(calc_basin(content)) # 1317792
        #visualize(content)