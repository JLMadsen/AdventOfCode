N,E,S,W = (-1,0),(0,1),(1,0),(0,-1)
pipes = {'|': [N, S],
         '-': [E, W],
         'L': [N, E],
         'J': [N, W],
         '7': [S, W],
         'F': [S, E]}

def solve(grid):
    start = (0, 0)
    area = 0

    for y,line in enumerate(grid):
        for x,char in enumerate(line):
            if char == 'S': start = (y, x)

    path = [start]

    while 1:
        y, x = path[-1]

        if (y,x) == start:
            if len(path) > 1: break
            for dy, dx in [N,E,S,W]:
                if grid[y+dy][x+dx] in pipes:
                    (ay, ax),(by, bx) = pipes[grid[y+dy][x+dx]]
                    if ((y+dy+ay, x+dx+ax) == start or 
                        (y+dy+by, x+dx+bx) == start): 
                        path.append((y+dy, x+dx))
                        area += x * dy
                        break
        else:
            pipe = grid[y][x]
            (ay, ax),(by, bx) = pipes[pipe]
            a, b = (y+ay, x+ax), (y+by, x+bx)
            target = a if a != path[-2] else b
            area += x * (ay if target == a else by)
            path.append(target)

    print(len(path)//2)            # 6979
    print(area - len(path)//2 + 1) # 442

if __name__ == "__main__":
    with open('input/day10.txt') as f:
        content = f.read().splitlines()
        solve(content) 