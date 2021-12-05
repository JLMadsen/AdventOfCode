from collections import defaultdict

def find_vents(coords):
    vents = defaultdict(lambda: 0)

    for c in coords:
        a, _, b = c.split(' ')
        x1, y1 = map(int, a.split(','))
        x2, y2 = map(int, b.split(','))

        if not (x1 == x2 or y1 == y2):
            continue

        if x1 == x2:
            l, h = sorted([y1, y2])
            vents[(x1, l)] += 1
            for i in range(1, h-l+1):
                vents[(x1, l + i)] += 1
        else:
            l, h = sorted([x1, x2])
            vents[(l, y1)] += 1
            for i in range(1, h-l+1):
                vents[(l + i, y1)] += 1

    count = 0
    for key, value in vents.items():
        if value > 1:
            count += 1

    return count

def find_vents2(coords):
    vents = defaultdict(lambda: 0)

    for c in coords:
        a, _, b = c.split(' ')
        x1, y1 = map(int, a.split(','))
        x2, y2 = map(int, b.split(','))

        if x1 == x2:
            l, h = sorted([y1, y2])
            vents[(x1, l)] += 1
            for i in range(1, h-l+1):
                vents[(x1, l + i)] += 1
        elif y1 == y2:
            l, h = sorted([x1, x2])
            vents[(l, y1)] += 1
            for i in range(1, h-l+1):
                vents[(l + i, y1)] += 1
        else:          
            a1, a2 = [x1, y1] if x1 < x2 else [x2, y2]
            b1, b2 = [x1, y1] if x1 > x2 else [x2, y2]

            yd = a1 - b1
            xd = a2 - b2

            xd, yd = xd//abs(xd), yd//abs(yd)

            if xd == -1 and yd == -1:
                xd, yd = 1, 1

            diff = b1 - a1

            for i in range(0, (diff+1)):
                pos = (a1+(xd*i), a2+(yd*i))
                vents[pos] += 1

    count = 0
    for key, value in vents.items():
        if value > 1:
            count += 1

    print_map(vents)
    return count

def print_map(vents):
    with open('map.txt', 'w') as f:
        for i in range(10):
            for j in range(10):
                f.write( str(vents[(j, i)] or '.') )
            f.write("\n")

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().split('\n')[:-1]

        print(find_vents(content)) # 6572
        print(find_vents2(content))