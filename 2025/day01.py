def part1(content, value=50, zeros=0):

    for d, n in map(lambda l: (l[0], int(l[1:])), content):
        value = (value + (n * (1 - 2 * (d == 'R')))) % 100
        zeros += not value

    print(zeros)

def part2(content, value=50, zeros=0):

    for d, n in map(lambda l: (l[0], int(l[1:])), content):
        r = int(n / 100)
        O = value == 0
        value += (n - (100 * r)) * (1 - 2 * (d == 'R'))
        zeros += ((value <= 0 and not O) or value > 99) + r
        value %= 100

    print(zeros)

if __name__ == "__main__":
    with open('input/day01.txt') as f:
        content = f.read().splitlines()
        part1(content) # 1141
        part2(content) # 6634
