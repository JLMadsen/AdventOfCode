N,E,S,W = (-1,0), (0,1), (1,0), (0,-1)
pipes = {'|': [N, S], '-': [E, W], 'L': [N, E], 
         'J': [N, W], '7': [S, W], 'F': [S, E]}

def solve(grid, area=0):
    start = [(y,l.index('S'))for y,l in enumerate(grid)if'S'in l][0]   
    path = [start]

    while 1:
        y, x = path[-1]

        if (y, x) == start:
            if len(path) > 1: break
            for dy, dx in [N,E,S,W]:
                if grid[y+dy][x+dx] in pipes:
                    (ay, ax),(by, bx) = pipes[grid[y+dy][x+dx]]
                    if start in [(y+dy+ay,x+dx+ax),(y+dy+by,x+dx+bx)]: 
                        path.append((y+dy, x+dx))
                        area += x * dy
                        break
        else:
            (ay, ax), (by, bx) = pipes[grid[y][x]]
            a, b = (y+ay, x+ax), (y+by, x+bx)
            path.append(a if a != path[-2] else b)
            area += x * (ay if path[-1] == a else by)

    print(len(path)//2)            # 6979
    print(area - len(path)//2 + 1) # 443

if __name__ == "__main__":
    with open('input/day10.txt') as f:
        content = f.read().splitlines()
        solve(content) 