import re
def card(line):
    n = list(map(int, re.findall(r'\d+',line)))
    return (n.pop(0), len(set(n[:10]).intersection(n[10:])))

def solve(content, value=0, alg={}):
    for id, wins in map(card, content):
        value += int(2**(wins-1))
        alg[id]=[1,[*range(id+1,id+wins+1)]]

    for count, to in alg.values():
        for target in to:
            alg[target][0] += count

    print(value)                          # 32609
    print(sum(a for a,b in alg.values())) # 14624680

if __name__ == "__main__":
    with open('input/day04.txt') as f:
        content = f.read().splitlines()
        solve(content)