from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

def diagonal(content, func):
    grouping = defaultdict(list)
    for y in range(len(content)):
        for x in range(len(content[y])):
            grouping[func(x,y)].append(content[y][x])
    return list(map(grouping.get, sorted(grouping)))

def part1(content):
    count = lambda string: (''.join(string)).count('XMAS')
    print(
        sum(
            sum(
                count(line) + count(line[::-1])
                for line in
                direction
            )
            for direction in [content, 
                [nth(content, i) for i in range(len(content))],
                diagonal(content, lambda x,y: x + y),
                diagonal(content, lambda x,y: x - y)]
        )
    ) # 2662

def part2(content, value=0):
    for y in range(len(content) - 2):
        for x in range(len(content[0]) - 2):
            grid = (content[y][x] + 
                    content[y][x+2] +
                    content[y+1][x+1] + 
                    content[y+2][x] + 
                    content[y+2][x+2])

            value += any(
                all(
                    a == b
                    for a, b in
                    zip(perm, grid)
                )
                for perm in ['MSAMS',
                             'SMASM',
                             'SSAMM',
                             'MMASS']
            )
    print(value) # 2034

if __name__ == "__main__":
    with open('input/day04.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
