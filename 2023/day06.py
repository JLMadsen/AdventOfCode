import math

def solve(content, pt2=0):
    print(math.prod([sum([i*(t-i)>d for i in range(t)]) for t,d in zip(*map(lambda y:[int(''.join(y))] if pt2 else[*map(int, y)],map(lambda x:x.split(':')[-1].split(),content)))]))

if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().splitlines()
        solve(content)    # 1624896
        solve(content, 1) # 32583852