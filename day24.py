import copy

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
                if layout[yn][xn] == '#':           bugCount += 1
                
            # A bug dies unless there is exactly one bug adjacent to it.
            # An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
            if layout[y][x] == '#' and bugCount != 1:       newLayout[y][x] = '.'
            elif layout[y][x] == '.' and bugCount in [1,2]: newLayout[y][x] = '#'
                
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
<<<<<<< HEAD
    minutes = 0
    while 1:        
=======
    while 1:
        
>>>>>>> 3d106db15e6054d0a8cd00d914085fb204a710fb
        if previous:
            for layout2 in previous:
                if layout == layout2:
                    return bioDiversity(layout)
        
        previous.append(layout)
        layout = step(layout)

def main() -> None:
    filename = 'input/day24input.txt'
    layout = open(filename).read().split()
    
    # string -> char array
    for i in range(len(layout)):
        layout[i] = [char for char in layout[i]]
        
    print('Part 1', part1(layout))
    
if __name__ == '__main__':
    assert bioDiversity(['.....', '.....', '.....', '#....', '.#...']) == 2129920, "Biodiversity calc failed"
    main()