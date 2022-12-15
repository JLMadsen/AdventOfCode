import re
nth = lambda arr, n: [*zip(*arr)][n-1]
manhatten = lambda x1, y1, x2, y2: abs(x1-x2) + abs(y1-y2)

def part1(content, y):
    value = 0
    sensors = set()
    beacons = set()
    distances = {(0,0):0}

    xmax = float('-inf')
    xmin = float( 'inf')
    
    for line in content:
        x1, y1, x2, y2 = map(int, re.findall('-?\d+', line))
        sensors.add((x1, y1))
        beacons.add((x2, y2))

        dist = manhatten(x1, y1, x2, y2)

        xmax = max(xmax, x1 + dist)
        xmin = min(xmin, x1 - dist)
        distances[(x1, y1)] = dist

    print('xmax', xmax)
    print('xmin', xmin)
    print('height', y)

    blocked = set()

    for x in range(xmin + xmin, xmax + xmax):
        # print('>', x)

        for sensor in sensors:
            if (manhatten(x, y, *list(sensor)) <= distances[sensor] and (x,y) not in beacons):

                blocked.add((x, y))
                break

    print(len(blocked))

# 4219347



    # print(sorted(nth(list(blocked), 1)))

    # lower = 0
    # upper = 0

    # for i in range(xmin, xmax + 1):
    #     found = False
    #     for sensor in sensors:
    #         # print(str(sensor).ljust(5 + len(str(xmax)) * 2), '>' , (i, y), '=', manhatten(i, y,*list(sensor)))
    #         if manhatten(i, y,*list(sensor)) <= distances[sensor]:
    #             lower = i
    #             found = True
    #             break
    #     if found: print('break lower', i, sensor, lower); break

    # print('_')
    # for i in range(xmin, xmax + 1):
    #     j = xmax - i
    #     found = False
    #     for sensor in sensors:
    #         # print(str(sensor).ljust(5 + len(str(xmax)) * 2), '>' , (j, y), '=', manhatten(j, y,*list(sensor)))
    #         if manhatten(j, y,*list(sensor)) <= distances[sensor]:
    #             upper = xmax - j
    #             found = True
    #             break
    #     if found: print('break upper', j); break

    # print(lower, upper)
    # print(xmax - lower - upper)

# 4017809 <
# 4017811 <
# 4030974 < 

ex = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""    

def part2(content, y):
    pass

if __name__ == "__main__":
    with open('input/day15.txt') as f:
        content, y = f.read().splitlines(), 2_000_000
        # content, y= ex.splitlines(), 10

        part1(content, y)
        part2(content, y)
