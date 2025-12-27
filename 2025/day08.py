from math import sqrt

def part1(content, remaining_steps=1000):
    distances = []

    for i, line in enumerate(content):
        for line2 in content[i + 1:]:
            box1 = x1, y1, z1 = tuple(map(int, line.split(',')))
            box2 = x2, y2, z2 = tuple(map(int, line2.split(',')))
            distance = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            distances.append([distance, box1, box2])

    sorted_distances = sorted(distances, key=lambda x: x[0])
    circuits = []

    for _, a, b in sorted_distances:
        ai = [a in c for c in circuits]
        bi = [b in c for c in circuits]

        if not any(ai) and not any(bi):
            circuits.append([a, b])

        elif ai == bi: pass
        
        elif any(ai) and any(bi):
            ai = ai.index(1)
            bi = bi.index(1)
            circuits[ai].extend(circuits[bi])
            circuits.pop(bi)

        elif any(ai) and not any(bi):
            circuits[ ai.index(1) ].append(b)

        elif any(bi) and not any(ai):
            circuits[ bi.index(1) ].append(a)

        remaining_steps -= 1
        if not remaining_steps:
            break

    lengths = [*map(len,circuits)]
    lengths.sort(reverse=1)

    value = 1
    for l in lengths[:3]:
        value *= l

    print(value)

def part2(content):
    boxes = []
    distances = []

    for i, line in enumerate(content):
        for line2 in content[i + 1:]:
            box1 = x1, y1, z1 = tuple(map(int, line.split(',')))
            box2 = x2, y2, z2 = tuple(map(int, line2.split(',')))

            if box1 not in boxes:
                boxes.append(box1)

            if box2 not in boxes:
                boxes.append(box2)

            distance = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            distances.append([distance, box1, box2])

    sorted_distances = sorted(distances, key=lambda x: x[0])
    circuits = []

    for _, a, b in sorted_distances:

        ai = [a in c for c in circuits]
        bi = [b in c for c in circuits]

        if not any(ai) and not any(bi):
            circuits.append([a, b])

        elif ai == bi:
            pass
        
        elif any(ai) and any(bi):
            ai = ai.index(1)
            bi = bi.index(1)
            circuits[ai].extend(circuits[bi])
            circuits.pop(bi)

        elif any(ai) and not any(bi):
            circuits[ ai.index(1) ].append(b)

        elif any(bi) and not any(ai):
            circuits[ bi.index(1) ].append(a)

        if len(circuits[0]) == len(boxes):
            print(a[0] * b[0])
            break

if __name__ == '__main__':
    with open("./input/day08.txt") as f:
        content = f.read().splitlines()
        part1(content) # 66640
        part2(content) # 78894156