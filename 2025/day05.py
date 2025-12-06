def part1(content):
    value = 0
    ranges = []

    for line in content:
        if line == '':
            continue

        if '-' in line:
            ranges.append([*map(int, line.split('-'))])
        else:
            for a, b in ranges:
                if a <= int(line) <= b:
                    value += 1
                    break

    print(value)

def part2(content):
    value = 0
    ranges = []

    for line in content:
        if '-' in line:
            ranges.append([*map(int, line.split('-'))])

    ranges.sort(key=lambda x: x[0])
    new_ranges = [ranges[0]]

    for a, b in ranges[1:]:
        x, y = new_ranges[-1]

        if a <= y:
            new_ranges[-1][1] = max(y, b)
        else:
            new_ranges.append([a, b])

    for a, b in new_ranges:
        value += b - a + 1

    print(value)
    
if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().splitlines()
        part1(content) # 868
        part2(content) # 354143734113772
