value     = lambda char: ord(char.lower()) - ord('`') + (26 * char.isupper())
split     = lambda x: (x[:len(x)//2], x[len(x)//2:])
intersect = lambda xs: set.intersection(*map(set, xs)).pop()

def solve(func, loop):
    print(sum([value(intersect(func(line))) for line in loop]))

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        solve(split, content) # 8139
        solve(lambda x: content[x:x+3], range(0, len(content), 3)) # 2668