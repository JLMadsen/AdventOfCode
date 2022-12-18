def adjacent(x,y,z):
    return [(x+1,y,z), (x-1,y,z),
            (x,y+1,z), (x,y-1,z),
            (x,y,z+1), (x,y,z-1)]

def solve(content, drops = set()):
    max_coordinate = 0

    for line in content:
        x, y, z = map(int, line.split(','))
        drops.add((x, y, z))
        max_coordinate = max([max_coordinate, x, y, z])

    surface_area = 0
    for point in drops:
        surface_area += sum([side not in drops for side in adjacent(*point)])
    print(surface_area) # 4604

    def bfs():
        global water
        water = set()
        queue = [(0,0,0)]
        while queue:
            current = queue.pop()
            water.add(current)

            for side in adjacent(*current):
                if (side not in drops and
                    side not in water and
                    all(-1 <= n <= (max_coordinate + 1) for n in side)):
                    queue.append(side)
    bfs()

    cooled_area = 0
    for point in drops:
        cooled_area += sum([side in water for side in adjacent(*point)])
    print(cooled_area) # 2604
        
if __name__ == "__main__":
    with open('input/day18.txt') as f:
        content = f.read().splitlines()
        solve(content)