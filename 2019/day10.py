import math

def getLineOfSigth(tab, pos):
    
    asteroids = {}
    
    # check other asteroids for Line of sight angle
    for y1 in range(len(tab)):
        for x1 in range(len(tab[y1])):
            
            if y1 == pos[1] and x1 == pos[0]: continue
            if tab[y1][x1] != '#' : continue
            
            delta_y = y1 - pos[1]
            delta_x = x1 - pos[0]
            angle = math.atan2(delta_y, delta_x)
            
            # if new angle, add to list
            # if angle already exists, it is blocked
            if angle not in asteroids.keys():
                asteroids[angle] = [x1, y1]
                
    return asteroids

def detectorPos(tab):
        
    #   detected, pos
    highest = [0, [0,0]]
    
    # traverse asteroids
    for y in range(len(tab)):
        for x in range(len(tab[y])):
            
            if tab[y][x] != '#':
                continue
            
            asteroids = getLineOfSigth(tab, [x,y])
            
            total = len(asteroids)
            if total > highest[0]:
                highest = [total, [x,y]]
                                
    return highest

def vaporize(tab, pos):
    
    shotCount = 0
    while 1:
        
        asteroids = getLineOfSigth(tab, pos)
        tab[pos[1]][pos[0]] = 'X'
        
        # sorted list of angles
        angles = asteroids.keys()
        angles = sorted ( angles )
        
        mid = 0
        for i in range(len(angles)-1):
            if angles[i] < -0.5*math.pi and angles[i+1] >= -0.5*math.pi:
                mid = i+1
        
        angles2 = angles[mid:] + angles[:mid]
        
        for angle in angles2:
            shotCount += 1
            
            pos = asteroids[angle]
            if shotCount == 200:
                return pos
            
            tab[pos[1]][pos[0]] = str(shotCount%10)

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
    assert result[0] == 33 and str(result[1]) == "[5, 8]", 'Test failed'

def main():
    Test()
    filename = '2019/input/day10input.txt'
    tab = open(filename).read().split('\n')
    
    ntab = []
    for row in tab:
        ntab.append(list(row))
    tab = ntab

    result = detectorPos(tab.copy())
    
    print('Part 1')
    print('Detected', result[0], 'asteroids from pos', str(result[1]))
    
    result = vaporize(tab.copy(), result[1])
    
    print('\nPart 2')
    print(result[0] * 100 + result[1])

if __name__ == '__main__':
    main()
