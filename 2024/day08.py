from collections import defaultdict

def inside(node, content):
    return (0 <= node[1] < len(content) and
            0 <= node[0] < len(content[0]))

def solve(content, pt2 = False):
    frequencies = defaultdict(list)
    antinodes = set()

    for y, line in enumerate(content):
        for x, char in enumerate(line):
            if char != '.':
                frequencies[char].append((x, y))

    for nodes in frequencies.values():
        for a in nodes:
            for b in [n for n in nodes if n != a]:
                ax, ay = a
                bx, by = b
                dx = ax - bx
                dy = ay - by

                if pt2:
                    while 1:
                        node_a = (ax + dx, ay + dy)
                        node_b = (bx + dx, by + dy)
                        dx += ax - bx
                        dy += ay - by

                        if (not inside(node_a, content) and 
                            not inside(node_b, content)):
                            break

                        antinodes.add(node_a)
                        antinodes.add(node_b)
                else:
                    node_a = (ax + dx, ay + dy)
                    if node_a != a and node_a != b:
                        antinodes.add(node_a)

    print(len([*filter(lambda n: inside(n, content), antinodes)]))
        # 278
        # 1067

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().splitlines()
        solve(content)
        solve(content, 1)