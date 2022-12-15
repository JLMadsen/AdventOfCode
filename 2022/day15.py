import re
manhatten = lambda x1, y1, x2, y2: abs(x1-x2) + abs(y1-y2)

def parse(content):
    beacons, sensors = set(), set()
    distances = {(0,0):0}
    xmax, xmin = float('-inf'), float( 'inf')
    for line in content:
        x1, y1, x2, y2 = map(int, re.findall('-?\d+', line))
        sensors.add((x1, y1))
        beacons.add((x2, y2))
        dist = manhatten(x1, y1, x2, y2)
        xmax, xmin = max(xmax, x1 + dist), min(xmin, x1 - dist)
        distances[(x1, y1)] = dist
    return beacons, sensors, distances, xmax, xmin

def part1(content, y, blocked = set()):
    beacons, sensors, distances, xmax, xmin = parse(content)
    for x in range(xmin, xmax):
        for sensor in sensors:
            if (manhatten(x, y, *sensor) <= distances[sensor] and 
               (x,y) not in beacons):
                blocked.add((x, y))
                break
    print(len(blocked))

def part2(content, y, sensors = set(), beacons = set()):
    beacons, sensors, distances, xmax, xmin = parse(content)
    for x in range(y + 1):
        dy = 0
        while dy <= y:
            for sensor in sensors:
                if ((delta := manhatten(x, dy, *sensor)) <= distances[sensor] or 
                   (x,dy) in beacons):
                    if dy < sensor[1]: dy += abs(dy-sensor[1])*2
                    else:              dy += distances[sensor] - delta
                    break
            else:
                return print(x*int(4e6)+dy)
            dy += 1

# SUPER SLOW, To be refactored.
if __name__ == "__main__":
    with open('input/day15.txt') as f:
        content, y = f.read().splitlines(), int(2e6)
        part1(content, y) # 5125700
        part2(content, y*2) # 11379394658764
