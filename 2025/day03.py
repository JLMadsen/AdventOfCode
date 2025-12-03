
def part1(content):
    value = 0
    for line in content:
        joltage = 0

        for i, a in enumerate(line[:-1]):
            for b in line[i + 1:]:
                joltage = max(joltage, int(a + b))

        value += joltage

    print(value)

# thanks Trong
def part2(content):
    value = 0
    length = 12

    for line in content:
        batteries = line[:length]

        for i in range(len(line) - length):
            joltage = int(batteries)
            batteries += line[length + i]

            for j in range(length):
                potential_batteries = batteries[:j] + batteries[j+1:]

                if joltage <= int(potential_batteries):
                    batteries = potential_batteries

            batteries = batteries[:length]

        value += int(batteries)

    print(value)

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
