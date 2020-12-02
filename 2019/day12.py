import re

class moon:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0
        
def printMoon(moon, vel = True):
    p = 'pos=<x='+ str(moon.x) +', y='+ str(moon.y) +', z='+ str(moon.z) +'>, '
    v = 'vel=<x='+ str(moon.v_x) +', y='+ str(moon.v_y) +', z='+ str(moon.v_z) +'>'
    
    out = p+v if vel else p
    
    print(out)
        
def calcGravity(moons):
     
    for i in range(len(moons)):
        current = moons[i]
         
        for j in range(len(moons)):             
            moon = moons[j]
            
            if current.x < moon.x:
                current.v_x += 1
            elif current.x > moon.x:
                current.v_x -= 1
            
            if current.y < moon.y:
                current.v_y += 1
            elif current.y > moon.y:
                current.v_y -= 1
                
            if current.z < moon.z:
                current.v_z += 1
            elif current.z > moon.z:
                current.v_z -= 1
                
def moveMoons(moons):
    
    for moon in moons:
        moon.x += moon.v_x
        moon.y += moon.v_y
        moon.z += moon.v_z
    
def calcEnergy(moons, steps):
    
    #print('\nAfter', 0, 'steps:')
    #for moon in moons:
    #    printMoon(moon)
    
    for i in range(steps):
        
        calcGravity(moons)
        moveMoons(moons)
        
        #print('\nAfter', (i+1), 'steps:')
        #for moon in moons:
        #    printMoon(moon)
        
    energy = 0
    for moon in moons:
        posEnergy = abs(moon.x) +   abs(moon.y) +   abs(moon.z)
        vecEnergy = abs(moon.v_x) + abs(moon.v_y) + abs(moon.v_z)
        
        energy += posEnergy * vecEnergy
        
    return energy
    
def timeForLoop(moons):
    history = []
    time = 0
    
    checkstring = ""
    for moon in moons:
        checkstring += str(moon.x) + " " + str(moon.y) + " "+ str(moon.z) + " "
    history.append(checkstring)
        
    #print('\nstart')
    #for moon in moons:
    #    printMoon(moon, False)
        
    while 1:
        time += 1
        
        calcGravity(moons)
        moveMoons(moons)

        checkstring = ""
        for moon in moons:
            checkstring += str(moon.x) + " " + str(moon.y) + " "+ str(moon.z) + " "
        

        if checkstring in history:
            print('\nend')
            for moon in moons:
                printMoon(moon, False)
                
            print(history)
            
            return time
        else:
            history.append(checkstring)
                      
        # check for test so it dont loop
        if time > 2772:
            exit('not working')

def getMoons(filename):
    text = open(filename).read()
    numbers = re.findall(r'-?\d+', text)
    num = list( map(int, numbers))
        
    moons = []
    for i in range(0,len(num),3):
        moons.append( moon(num[i], num[i+1], num[i+2]))
        
    return moons
            
def main():
    filename = '2019/input/day12test.txt'
    steps = 10
           
    moons = getMoons(filename)
        
    energy = calcEnergy(moons.copy(), steps)
    print('Part 1', energy)
    
    time = timeForLoop(moons)
    print('Part 2', time)
        
        
if __name__ == '__main__':
    main()