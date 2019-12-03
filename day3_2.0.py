# Warning! if you run this program you should know that it is not fast, but it will give right answer.
# Some optimizations have been made.

BIG_NUMBER = 9999999999999999

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

def readWires() -> []:

    cmd1, cmd2 = open('input/day3input.txt').read().split('\n')
    cmd1, cmd2 = cmd1.split(','), cmd2.split(',')
    if cmd1 == cmd2: exit('read error')
    return cmd1, cmd2

def getVec(char) -> [int, int]:
    if char == 'R':
        return [1,0]
    elif char == 'L':
        return [-1,0]
    elif char == 'U':
        return [0,1]
    else:
        return [0,-1]

def getPathAndIntersections(cmd1, cmd2) -> []:
    p1, p2, cur = [], [], [1,1]
    intersections = []

    for cmd in cmd1:
        vec = getVec(cmd[0])
        dist = int(''.join(cmd[1::]))

        for i in range(dist):
        
            cur[0] += 1 * vec[0]
            cur[1] += 1 * vec[1]

            p1.append(cur.copy())

    for cmd in cmd2:
        vec = getVec(cmd[0])
        dist = int(''.join(cmd[1::]))

        for i in range(dist):
        
            cur[0] += 1 * vec[0]
            cur[1] += 1 * vec[1]

            if cur in p1 and cur != [1,1]:
                intersections.append(cur.copy())
            p2.append(cur.copy())

    return p1, p2, intersections

def main() -> None:

    cmd1, cmd2 = readWires()
    p1, p2, inters = getPathAndIntersections(cmd1, cmd2)

    print('part 1')
    print('Closest by skyline:', skylineIntersection(inters))

    print('part 2')
    print('Closest by step:', stepIntersection(p1, p2, inters))

if __name__ == '__main__':
    main()