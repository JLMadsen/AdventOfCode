from copy import deepcopy

def part1(content):
    value = 0
    content = [[*r] for r in content]
    content[1][content[0].index('S')] = '|'

    for i in range(len(content)):
        line = content[i]

        for j, char in enumerate(line):
            if char == '^' and content[i-1][j] == '|':
                content[i][j-1] = '|'
                content[i][j+1] = '|'
                value += 1

            elif content[i-1][j] == '|':
                content[i][j] = '|'

    print(value)

def part2(content):
    splitters = []

    for char in content[0]:
        splitters.append(char == 'S')

    for line in content[1:]:
        for i, visited in enumerate([*splitters]):
            if line[i] == '^':
                
                # count how many paths end up at each splitter
                splitters[i+1] += visited
                splitters[i-1] += visited

                # clear beam origin
                splitters[i] = 0

    print(sum(splitters))

if __name__ == "__main__":
    with open('input/day07.txt') as f:
        content = f.read().splitlines()
        part1(content) # 1573
        part2(content) # 15093663987272
