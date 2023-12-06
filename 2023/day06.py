def solve(content, pt2=0, value=1):
    content = [*map(lambda y: [int(''.join(y))] if pt2 else [*map(int, y)],map(lambda x: x.split(':')[-1].split(), content))]
    for t, d in zip(*content):
        value *= sum([i*(t-i) > d for i in range(t)])
    print(value)

if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().splitlines()
        solve(content)    # 1624896
        solve(content, 1) # 32583852