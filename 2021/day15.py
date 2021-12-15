from collections import defaultdict
from queue import PriorityQueue

def adjacent(grid, i, j, ):
    return [[y, x] for a, b in [(1,0), (0,1), (-1,0),(0,-1)] if not ( (x := a + j) < 0 or (y := b + i) < 0 or x >= len(grid[0]) or y >= len(grid) )]

def dijkstra(grid):
    w, h = len(grid), len(grid[0])
    Q = PriorityQueue()
    dist = defaultdict(lambda: float('inf'))
    start = (0, 0)
    dist[start] = 0
    Q.put((0, start))
    
    while not Q.empty():
        _, (y1, x1) = Q.get()

        if y1 == h - 1 and x1 == w - 1:
            return dist, (y1, x1)

        for y2, x2 in adjacent(grid, y1, x1):
            new_distance = dist[(y1, x1)] + grid[y2][x2]

            if new_distance < dist[(y2, x2)]:
                dist[(y2, x2)] = new_distance
                Q.put((new_distance, (y2, x2)))

if __name__ == "__main__":
    with open('input/day15.txt') as f:
        content = f.read().split('\n')[:-1]
        grid = [[*map(int, line)] for line in content]

        dist, goal = dijkstra(grid)
        print(dist[goal]) # 595

        big_grid = [line[:] for line in grid]
        for i in range(len(grid)):
            for j in range(1, 5):
                big_grid[i] += [ value + j if (value + j) < 10 else (value + j) % 10 + 1 for value in grid[i] ]

        for i in range(1, 5):
            for j in range(len(grid)):
                big_grid.append([value + i if (value + i) < 10 else (value + i) % 10 + 1 for value in big_grid[j]])

        dist, goal = dijkstra(big_grid)
        print(dist[goal]) # 2914