import re

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
        value += int(2**(len(wins.intersection(bets))-1))
    print(value)

def part2(content, value=0):
    alg = {}
    high = 0

    for line in content:
        id, wins, bets = card(line)
        alg[id] = [1, [*range(id+1, id+len(wins.intersection(bets))+1)]]
        value += 1
        high = id
    
    for i in range(1, high+1):
        count, to = alg[i]
        for target in to:
            obj = alg[target]
            alg[target] = [obj[0] + count, obj[1]]
            value += count
        alg[i] = [0, to]

    print(value)

if __name__ == "__main__":
    with open('input/day04.txt') as f:
        content = f.read().splitlines()
        part1(content) # 32609
        part2(content) # 14624680