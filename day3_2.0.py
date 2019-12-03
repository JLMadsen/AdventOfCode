def draw(path1, path2, cmd, cur, wire2) -> []:
    try:
        dir = cmd[0]
        dist = int(''.join(cmd[1::]))
    except:
        exit(cmd)
    
    vec = [1,0]
    if(dir == 'U'):
        vec = [0,1]
    elif(dir == 'D'):
        vec = [0,-1]
    elif(dir == 'L'):
        vec = [-1, 0]

    for i in range(dist):
        
        cur[0] += 1 * vec[0]
        cur[1] += 1 * vec[1]

        if not wire2:
            path1.append(cur.copy())
        else:
            path2.append(cur.copy())
            
    return [path1, path2, cur]

def readMap() -> []:
    cmds = open('day3input.txt').read().split(',')

    path1 = []
    path2 = []
    
    # start
    cur = [1,1]
    wire2 = False
    for cmd in cmds:
        
        if '\n' in cmd:
            c1, c2 = cmd.split('\n')
            path1, path2, cur = draw(path1, path2, c1, cur, wire2)
            cur = [1,1]
            wire2 = True
            path1, path2, cur = draw(path1, path2, c2, cur, wire2)
            continue

        path1, path2, cur = draw(path1, path2, cmd, cur, wire2)

    return [path1, path2]

def findIntersections(path1, path2) -> []:
    print(len(path1))
    print(len(path2))
    res = []
    for pos in path1:
        if pos == [1,1] or pos in res: continue
        if pos in path2:
            res.append(pos)
    return res

def taxiCab(start, goal) -> int:
    return abs(goal[0]-start[0]) + abs(goal[1]-start[1])

def findClosestInt(intersections):
    closest = [1,1]
    dist = 99999
    for inter in intersections:
        if taxiCab([1,1], inter) < dist:
            closest = inter
            dist = taxiCab([1,1], inter)
            
    if dist == 99999:
        exit('No intersection found')
    return dist

def main() -> None:
    path1, path2 = readMap()
    intersections = findIntersections(path1, path2)
    dist = findClosestInt(intersections)

    print('Distance =', dist)
    
if __name__ == '__main__':
    main()