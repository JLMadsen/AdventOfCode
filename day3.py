def draw(map, cmd, cur) -> []:
    dir = cmd[0]
    dist = int(''.join(cmd[1::]))
    
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

        if cur[0] >= len(map):
            for j in range(dist):
                map.append([0]*len(map[0]))

        if cur[1] >= len(map[0]):
            for j in range(len(map)):
                for h in range(dist):
                    map[j].append(0)

        try:
            map[cur[0]][cur[1]] += 1
        except:
            exit('Error, Index out of bounds\ndir: '+ dir +' cur: ['+ str(cur[0]) +', '+ str(cur[1]) +'] size: ['+ str(len(map)) +', '+ str(len(map[0])) +']')

    return [map, cur]

def readMap() -> []:
    cmds = open('day3input.txt').read().split(',')

    map = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
    
    # start
    map[1][1] = -1
    cur = [1,1]

    for cmd in cmds:
        
        if '\n' in cmd:
            c1, c2 = cmd.split('\n')
            map, cur = draw(map, c1, cur)
            cur = [1,1]
            map, cur = draw(map, c2, cur)
            continue

        map, cur = draw(map, cmd, cur)

    return map

# bfs search ish, dont care about edges
def BFS(map) -> []:

    side = 0
    if len(map) > len(map[0]):
        side = len(map)
    else:
        side = len(map[0])

    for i in range(1, side):
        offset = i
        length = i + 1

        cur = [offset, 1]
        for j in range(length):
            count = map[cur[0]][cur[1]]

            if count > 1:
                return [cur[0], cur[1]]
            cur[1] += 1

        cur = [1, offset]
        for j in range(length):
            count = map[cur[0]][cur[1]]

            if count > 1:
                return [cur[0], cur[1]]
            cur[0] += 1

def taxiCab(start, goal) -> int:
    return abs(goal[0]-start[0]) + abs(goal[1]-start[1])

def main() -> None:
    map = readMap()

    dist = taxiCab([1,1], BFS(map))
    print('Distance =', dist)
    
if __name__ == '__main__':
    main()