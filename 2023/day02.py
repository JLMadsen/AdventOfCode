from collections import defaultdict
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

def part1(content, value = 0):
    for line in content:
        id, games = line.split(':')
        done = False

        for game in games.split(';'):
            count = defaultdict(lambda: 0)
            for color in game.split(','):
                num, col = color.strip().split(' ')
                count[col] += int(num)

            if not all(v <= max_cubes[k] for k, v in count.items()):
                done = True

        if not done: value += int(id.split(' ')[-1])
    print(value)

def part2(content, value = 0):
    for line in content:
        count = defaultdict(lambda: 0)
        id, games = line.split(':')

        for game in games.split(';'):
            for color in game.split(','):
                num, col = color.strip().split(' ')
                count[col] = max(int(num), count[col])

        m = 1
        for c in count.values():
            m *= c

        value += m
    print(value)

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().splitlines()
        part1(content) # 2105
        part2(content) # 72422
