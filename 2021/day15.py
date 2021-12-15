from collections import defaultdict
from queue import PriorityQueue

def adjacent(grid, i, j, ):
    return [[y, x] for a, b in [(1,0), (0,1), (-1,0),(0,-1)] if not ( (x := a + j) < 0 or (y := b + i) < 0 or x >= len(grid[0]) or y >= len(grid) )]

def djikstra(grid):
    w, h = len(grid), len(grid[0])
    Q = PriorityQueue()

    dist = defaultdict(lambda: float('inf'))
    prev = {}

    start = (0, 0)
    dist[start] = 0
    Q.put((0, start))
    
    while not Q.empty():
        #print('queue size', Q.qsize())

        weight, (y1, x1) = Q.get()
        #print('current', y1, x1)

        if y1 == h - 1 and x1 == w - 1:
            return dist, prev, (y1, x1)

        for y2, x2 in adjacent(grid, y1, x1):
            #print('next', y2, x2)
            
            #print(dist[(y1, x1)], grid[y2][x2])
            new_distance = dist[(y1, x1)] + grid[y2][x2]

            if new_distance < dist[(y2, x2)]:
                #print('has shorter distance')

                dist[(y2, x2)] = new_distance
                prev[(y2, x2)] = (y1, y2)

                Q.put((new_distance, (y2, x2)))

    print('Did not find goal')
    return None, None

test = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

if __name__ == "__main__":
    with open('input/day15.txt') as f:
        #content = f.read().split('\n')[:-1]
        content = test.split('\n')
        grid = [[*map(int, line)] for line in content]

        dist, prev, goal = djikstra(grid)
        print(dist[goal]) # x < 604

        # expand grid
        


        dist, prev, goal = djikstra(grid[:])
        print(dist[goal]) # x < 604