class Dir:
    def __init__(self):
        self.north = [ 1, 0]
        self.south = [-1, 0]
        self.east  = [ 0, 1]
        self.west  = [ 0,-1]

        self.compass = {'E': self.east, 'S': self.south, 'W': self.west, 'N': self.north }
        self.keys = [*self.compass.keys()]
        self.rot = lambda x, n, c: self.keys[(self.keys.index(c)+n//90 if 'R' in x else self.keys.index(c)-(n//90))%len(self.keys)]

dir = Dir()

def sail(data):
    current_direction = 'E'
    x = y = 0
    for inst in data:
        action, num = inst[0], int(inst[1:])

        if action in dir.keys:
            value = [*map(lambda x: x*num, dir.compass[action])]
            y, x = y+value[0], x+value[1]

        elif action in 'RL':
            current_direction = dir.rot(action, num, current_direction)

        elif action == 'F':
            value = [*map(lambda x: x*num, dir.compass[current_direction])]
            y, x = y+value[0], x+value[1]

    print(abs(x)+abs(y))

def waypoint(data):

    current_direction = 'E'
    x = y = 0
    wx, wy = 10, 1

    for inst in data:       
        action, num = inst[0], int(inst[1:])

        if action in dir.keys:

            value = [*map(lambda n: n*num, dir.compass[action])]
            wy, wx = wy+value[0], wx+value[1]

        elif action in 'RL':

            for _ in range(num//90 if action in 'R' else (360-num)//90):
                wx_ = wx
                wx = wy
                wy = -wx_

        elif action == 'F':

            value = [*map(lambda x: x*num, [wy, wx])]
            y, x = y+value[0], x+value[1]

    print(abs(x)+abs(y))       

if __name__ == "__main__":
    with open('2020/input/day12.txt') as f:

        data = f.read().splitlines()

        sail(data)     # 1589
        waypoint(data) # 23960