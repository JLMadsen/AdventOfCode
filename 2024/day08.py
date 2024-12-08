import math
from collections import defaultdict

def inside(node, content):
    return (
        node[1] >= 0 and node[1] < len(content[0]) and
        node[0] >= 0 and node[0] < len(content)
    )

def solve(content, pt2 = False):
    frequencies = defaultdict(list)
    antinodes = set()

    for y, line in enumerate(content):
        for x, char in enumerate(line):
            if char != '.':
                frequencies[char].append((x, y))

    for nodes in frequencies.values():
        for a in nodes:
            for b in nodes:
                if a == b:
                    continue

                ax, ay = a
                bx, by = b
                dx = ax - bx
                dy = ay - by

                if pt2:
                    gcd = math.gcd(dx, dy)
                    gcdx = dx // gcd
                    gcdy = dy // gcd

                    while 1:
                        node_a = (ax + dx, ay + dy)
                        node_b = (bx + dx, by + dy)
                        dx += gcdx
                        dy += gcdy

                        if (not inside(node_a, content) and 
                            not inside(node_b, content)):
                            break

                        if inside(node_a, content):
                            antinodes.add(node_a)
                        if inside(node_b, content):
                            antinodes.add(node_b)
                else:
                    node_a = (ax + dx, ay + dy)
                    node_b = (bx + dx, by + dy)
                    if node_a != a and node_a != b and inside(node_a, content):
                        antinodes.add(node_a)
                    if node_b != a and node_b != b and inside(node_b, content):
                        antinodes.add(node_b)

    print(len(antinodes))
        # 278
        # 1067

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().splitlines()
        solve(content)
        solve(content, 1)
