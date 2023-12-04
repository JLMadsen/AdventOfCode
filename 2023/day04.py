import re
scratch = lambda a,b: len(a.intersection(b))

def card(line):
    id, numbers = line.split(':')
    wins, bets = numbers.split('|')
    wins = set(map(int, re.findall(r'\d+', wins)))
    bets = set(map(int, re.findall(r'\d+', bets)))
    id = int(id.split()[-1])
    return (id, wins, bets)

def part1(content, value=0):
    for line in content:
        id, wins, bets = card(line)
        value += int(2**(scratch(wins,bets)-1))
    print(value)

def part2(content):
    alg = {}
    value = len(content)
    for line in content:
        id, wins, bets = card(line)
        alg[id] = [1, [*range(id+1, id+scratch(wins,bets)+1)]]
    
    for i in range(len(content)):
        count, to = alg[i+1]
        for target in to:
            obj = alg[target]
            alg[target] = [obj[0] + count, obj[1]]
            value += count
    print(value)

if __name__ == "__main__":
    with open('input/day04.txt') as f:
        content = f.read().splitlines()
        part1(content) # 32609
        part2(content) # 14624680