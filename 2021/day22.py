import re

clamp = lambda value: max(min(50, value), -50)

def reboot(instructions):
    cubes = {}

    for instruction in instructions:
        state, cube = instruction.split(' ')
        x, y, z = cube.split(',')

        x = list(map(int, re.findall(r'-?\d+', x)))
        y = list(map(int, re.findall(r'-?\d+', y)))
        z = list(map(int, re.findall(r'-?\d+', z)))

        if any([((a < -50 and b < -50) or (a >  50 and b >  50)) for a, b in [x, y, z]]):
            continue

        x = list(map(lambda n: clamp(n), x))
        y = list(map(lambda n: clamp(n), y))
        z = list(map(lambda n: clamp(n), z))

        x[1] += 1
        y[1] += 1
        z[1] += 1

        for dx in range(*x):
            for dy in range(*y):
                for dz in range(*z):
                    #print(dx, dy, dz)

                    cubes[(dx, dy, dz)] = 1 if 'on' in state else 0

    print(sum(cubes.values()))

from collections import Counter

def reboot2(instructions):
    # use counter instead of dict
    cubes = Counter()

    for instruction in instructions:
        # simpler extraction
        x1, x2, y1, y2, z1, z2 = list(map(int, re.findall(r'-?\d+', instruction)))
        state = 1 if 'on' in instruction else 0

        new_cubes = Counter()
        # intersect existing cubes
        for cube, old_state in cubes.items():
            #print(old_state)
            dx1, dx2, dy1, dy2, dz1, dz2 = cube

            intersect_x1 = max(x1, dx1)
            intersect_x2 = min(x2, dx2)
            intersect_y1 = max(y1, dy1)
            intersect_y2 = min(y2, dy2)
            intersect_z1 = max(z1, dz1)
            intersect_z2 = min(z2, dz2)

            if ( intersect_x1 <= intersect_x2 and 
                 intersect_y1 <= intersect_y2 and 
                 intersect_z1 <= intersect_z2 ):
                
                # new_cubes[(intersect_x1, intersect_x2, 
                #            intersect_y1, intersect_y2, 
                #            intersect_z1, intersect_z2)] = old_state * -1

                new_cubes[(intersect_x1, intersect_x2, 
                           intersect_y1, intersect_y2, 
                           intersect_z1, intersect_z2)] -= old_state
        
        new_cubes[(x1, x2, y1, y2, z1, z2)] += state

        cubes.update(new_cubes)

    counter = 0
    for cube, state in cubes.items():
        x1, x2, y1, y2, z1, z2 = cube
        # cancel out intersecting cubes
        counter += ( x2 - x1 + 1 ) * ( y2 - y1 + 1 ) * ( z2 - z1 + 1 ) * state

    print(counter)

if __name__ == "__main__":
    with open('input/day22.txt') as f:
        content = f.read().split('\n')[:-1]

        reboot(content) # 610196
        reboot2(content) # 1282401587270826
