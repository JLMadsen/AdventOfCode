# https://adventofcode.com/2019/day/3

BIG_NUMBER = 9999999999999999

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
    cmds = open('2019/input/day3input.txt').read().split(',')

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

    res = []
    for pos in path1:
        if pos == [1,1] or pos in res: continue
        if pos in path2:
            res.append(pos)
    return res

def stepIntersection(path1, path2, intersections) -> int:

    p1 = [0]*len(intersections)
    p2 = [0]*len(intersections)

    dist = 1
    for pos in path1:
        for i in range(len(intersections)):
            if pos == intersections[i]:
                p1[i] = dist
                break
        dist += 1

    dist = 1
    for pos in path2:
        for i in range(len(intersections)):
            if pos == intersections[i]:
                p2[i] = dist
                break
        dist += 1

    totalDistance = BIG_NUMBER
    for len1, len2 in zip(p1, p2):
        if (len1+len2) < totalDistance:
            totalDistance = (len1+len2)

    if totalDistance == BIG_NUMBER:
        exit('No intersection found')
    return totalDistance

def taxiCab(start, goal) -> int:
    return abs(goal[0]-start[0]) + abs(goal[1]-start[1])

def skylineIntersection(intersections):
    closest = [1,1]
    dist = BIG_NUMBER
    for inter in intersections:
        if taxiCab([1,1], inter) < dist:
            closest = inter
            dist = taxiCab([1,1], inter)
            
    if dist == BIG_NUMBER:
        exit('No intersection found')
    return dist

def main() -> None:

    path1, path2 = readMap()
    intersections = findIntersections(path1, path2)

    print('part 1')
    print('Closest by skyline:', skylineIntersection(intersections))

    print('part 2')
    print('Closest by step:', stepIntersection(path1, path2, intersections))

if __name__ == '__main__':
    main()