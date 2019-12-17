import math

def detectorPos(tab):
        
    #   detected, pos
    highest = [0, [0,0]]
    
    # traverse asteroids
    for y in range(len(tab)):
        for x in range(len(tab[y])):
            
            #print(x,y)
                        
            if tab[y][x] != '#':
                continue
            
            angles = []
            
            # check other asteroids for Line of sight angle
            for y1 in range(len(tab)):
                for x1 in range(len(tab[y1])):
                    
                    #if y1 == y and x1 == x: continue
                    if tab[y1][x1] != '#' : continue
                    
                    delta_y = y1 - y
                    delta_x = x1 - x
                    angle = math.atan2(delta_y, delta_x)
                    
                    # if new angle, add to list
                    # if angle already exists, it is blocked
                    if angle not in angles:
                        angles.append(angle)
                                                
            total = len(angles)
            if total > highest[0]:
                highest = [total, [x,y]]
                
    return highest
                    
def Test():
    test1 = ["......#.#.",
             "#..#.#....",
             "..#######.",
             ".#.#.###..",
             ".#..#.....",
             "..#....#.#",
             "#..#....#.",
             ".##.#..###",
             "##...#..#.",
             ".#....####",]
    
    result = detectorPos(test1)
    assert result[0] == 33 and str(result[1]) == "[5, 8]", 'Test 1 failed'

def main():
    Test()
    filename = 'input/day10input.txt'
    astroidMap = open(filename).read().split('\n')
        
    result = detectorPos(astroidMap)
    
    print('Part 1')
    print('Detected', result[0], 'asteroids from pos', str(result[1]))

if __name__ == '__main__':
    main()
