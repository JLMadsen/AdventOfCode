from collections import defaultdict

def find_vents(coords, diag=False):
    vents = defaultdict(lambda: 0)

    for c in coords:
        a, _, b = c.split(' ')
        x1, y1 = map(int, a.split(','))
        x2, y2 = map(int, b.split(','))

        if x1 == x2:
            l = min(y1, y2)
            vents[(x1, l)] += 1
            for i in range(1, max(y1, y2) - l + 1):
                vents[(x1, l + i)] += 1

        elif y1 == y2:
            l = min(x1, x2)
            vents[(l, y1)] += 1
            for i in range(1, max(x1, x2) - l + 1):
                vents[(l + i, y1)] += 1

        elif diag:
            a1, a2 = [x1, y1] if x1 < x2 else [x2, y2]
            b1, b2 = [x1, y1] if x1 > x2 else [x2, y2]

            yd = a1 - b1
            xd = a2 - b2

            xd, yd = xd // abs(xd), yd // abs(yd)

            if xd == -1 and yd == -1:
                xd, yd = 1, 1 

            for i in range(0, (b1 - a1 + 1)):
                vents[(a1 + (xd * i), a2 + (yd * i))] += 1

    return sum([ 1 if value > 1 else 0 for value in vents.values() ])

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().split('\n')[:-1]

        print(find_vents(content)) # 6572
        print(find_vents(content, True)) # 21466