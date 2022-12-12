from collections import defaultdict
from queue import PriorityQueue

START, GOAL = 'S', 'E'

def adjacent(size, i, j):
    return [[y, x] for a, b in [(1,0), (0,1), (-1,0),(0,-1)]
     if not ((x := a + j) < 0  or 
             (y := b + i) < 0  or 
              y >= size[0] + 1 or
              x >= size[1] + 1 )]

def dijkstra(grid, pt2 = False, start = (0,0), goal = (0,0), pt2_start = []):
    size = (len(grid) - 1, len(grid[0]) - 1)

    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            if v == START: start = (y, x)
            if v == GOAL:  goal = (y, x)
            if v == 'a':   pt2_start.append((y,x))

    Q = PriorityQueue()
    dist = defaultdict(lambda: float('inf'))

    if not pt2: Q.put((0, start))
    else: [Q.put((0, p)) for p in pt2_start ]

    if not pt2: dist[start] = 0
    else: [dist.__setitem__(p, 0) for p in pt2_start ]

    while not Q.empty():
        _, (y1, x1) = Q.get()
        height = grid[y1][x1]

        if (y1, x1) == goal:
            return print(dist[goal])
            
        for y2, x2 in adjacent(size, y1, x1):
            if y2 > size[0] or x2 > size[1]:
                continue  

            new_distance = dist[(y1, x1)] + 1
            next_height = grid[y2][x2]

            delta_height = ord(next_height) - ord(height) if height != START else -1
            if next_height == GOAL and height != 'z': continue
            if new_distance < dist[(y2, x2)] and delta_height < 2:
                dist[(y2, x2)] = new_distance
                Q.put((new_distance, (y2, x2)))

if __name__ == "__main__":
    with open('input/day12.txt') as f:
        content = f.read().splitlines()
        dijkstra(content) # 484
        dijkstra(content, True) # 478