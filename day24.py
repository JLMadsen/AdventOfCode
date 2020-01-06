import copy

def equals(lay1, lay2) -> bool:
    for i in range(len(lay1)):
        for j in range(len(lay1[0])):
            if lay1[i][j] != lay2[i][j]:
                return False
    return True

def printLayout(l, reversed = False) -> None: 
    if reversed:
        for j in l[::-1]: print(j)
    else:
        for j in l: print(j)

def neighbors(x, y) -> []:
    
    pos1 = [x-1, y]
    pos2 = [x+1, y]
    pos3 = [x, y+1]
    pos4 = [x, y-1]
    
    return [pos1, pos2, pos3, pos4]

def step(layout) -> []:
    newLayout = copy.deepcopy(layout)
    
    for y in range(len(layout)):
        for x in range(len(layout[0])):            
            bugCount = 0
            
            for xn, yn in neighbors(x, y):
                
                if xn < 0 or xn > len(layout[0])-1: continue
                if yn < 0 or yn > len(layout)-1:    continue
                
                neighbor = layout[yn][xn]
                if neighbor == '#': bugCount += 1
                
            # A bug dies unless there is exactly one bug adjacent to it.
            if layout[y][x] == '#':
                if bugCount != 1:
                    newLayout[y][x] = '.'
                    continue
            
            # An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
            if layout[y][x] == '.':
                if bugCount in [1,2]:
                    newLayout[y][x] = '#'
                    continue
                
    return newLayout
            
def bioDiversity(layout) -> int:
    diversity = 0
    
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            
            if layout[y][x] == '#':
                diversity += 2 ** (( y * len(layout[0])) + x )
                
    return diversity

def part1(layout) -> None:
    previous = []
    minutes = 0
    while 1:        
        if previous:
            for layout2 in previous:
                if equals(layout, layout2):
                    return bioDiversity(layout)
        
        previous.append(layout)
        layout = step(layout)
        minutes += 1

def main() -> None:
    filename = 'input/day24input.txt'
    layout = open(filename).read().split()
    #layout = ['....#','#..#.','#..##','..#..','#....',]
    
    # string -> char array
    for i in range(len(layout)):
        layout[i] = [char for char in layout[i]]
        
    res = part1(layout)
    print('Part 1', res)
    
if __name__ == '__main__':
    assert bioDiversity(['.....', '.....', '.....', '#....', '.#...']) == 2129920, "Biodiversity calc failed"
    main()