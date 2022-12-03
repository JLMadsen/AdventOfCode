value     = lambda char: ord(char.lower()) - ord('a') + 1 + (26 if char.isupper() else 0)
split     = lambda _, x: (x[:len(x)//2], x[len(x)//2:])
intersect = lambda xs: set.intersection(*map(set, xs)).pop()

def solve(content, func, loop):
    print(sum([value(intersect(func(content, line))) for line in loop]))

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        solve(content, split, content) # 8139
        solve(content, lambda x, i:x[i:i+3], range(0, len(content), 3)) # 2668