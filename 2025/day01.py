def part1(content):
    value = 50
    zeros = 0

    for line in content:
        d, n = line[0], int(line[1:])

        if d == 'R':
            value += n
        else:
            value -= n

        value = value % 100
        if value == 0:
            zeros += 1

    print(zeros)

def part2(content):
    value = 50
    zeros = 0

    for line in content:
        d, n = line[0], int(line[1:])

        for _ in range(n):
            if d == 'R':
                value += 1
            else:
                value -= 1

            value = value % 100

            if value == 0:
                zeros += 1

    print(zeros)

if __name__ == "__main__":
    with open('input/day01.txt') as f:
        content = f.read().splitlines()
        part1(content) # 1141
        part2(content) # 6634
