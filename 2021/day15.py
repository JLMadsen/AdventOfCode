from collections import defaultdict
from queue import PriorityQueue

def adjacent(size, i, j, ):
    return [[y, x] for a, b in [(1,0), (0,1), (-1,0),(0,-1)]
     if not ((x := a + j) < 0  or 
             (y := b + i) < 0  or 
              x >= size[0] + 1 or
              y >= size[1] + 1 )]

def dijkstra(grid):
    size = goal = (len(grid) - 1, len(grid[0]) - 1)
    start = (0, 0)

    Q = PriorityQueue()
    Q.put((0, start))
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    
    while not Q.empty():
        _, (y1, x1) = Q.get()

        if (y1, x1) == goal:
            return dist[goal]

        for y2, x2 in adjacent(size, y1, x1):
            new_distance = dist[(y1, x1)] + grid[y2][x2]

            if new_distance < dist[(y2, x2)]:
                dist[(y2, x2)] = new_distance
                Q.put((new_distance, (y2, x2)))

if __name__ == "__main__":
    with open('input/day15.txt') as f:
        content = f.read().split('\n')[:-1]
        grid = [[*map(int, line)] for line in content]

        print(dijkstra(grid)) # 595

        big_grid = [line[:] for line in grid]
        for i in range(len(grid)):
            for j in range(1, 5):
                big_grid[i] += [ value + j if (value + j) < 10 else (value + j) % 10 + 1 for value in grid[i] ]

        for i in range(1, 5):
            for j in range(len(grid)):
                big_grid.append([value + i if (value + i) < 10 else (value + i) % 10 + 1 for value in big_grid[j]])

        print(dijkstra(big_grid)) # 2914