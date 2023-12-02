import math
cubes = ['red','green','blue']

def solve(content, idsum=0, power=0):
    for line in content:
        _, id, *pairs = line.split()
        count = {c: 0 for c in cubes}

        for num, col in zip(pairs[::2], pairs[1::2]):
            if col[-1] in ';,': col = col[:-1]
            count[col] = max(count[col], int(num))

        if all(v <= cubes.index(k)+12 for k,v in count.items()):
            idsum += int(id[:-1])
        power += math.prod(count.values())

    print(idsum) # 2105
    print(power) # 72422

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().splitlines()
        solve(content)