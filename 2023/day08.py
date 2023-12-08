import math


def part1(content, value=0):
    lr = content[0]
    ways = {s:[l[1:-1],r[:-1]]for s,_,l,r in map(str.split,content[2:])}
    position = 'AAA'

    while position != 'ZZZ':       
        position = ways[position][lr[value % len(lr)] == 'R']
        value += 1

    print(value)

def part2(content, value=0, steps=[]):
    lr = content[0]
    ways = {s:[l[1:-1],r[:-1]]for s,_,l,r in map(str.split,content[2:])}
    ghosts = [node for node in ways.keys() if node[-1] == 'A']

    while len(ghosts) > 0:
        value += 1
        new_ghosts = []
        for node in ghosts:
            new = ways[node][lr[(value-1) % len(lr)]=='R']
            [new_ghosts,steps][l:=new[-1]=='Z'].append([new,value][l])
        ghosts = new_ghosts

    print(math.lcm(*steps))

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().splitlines()
        part1(content) # 17287
        part2(content) # 18625484023687