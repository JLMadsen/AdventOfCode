def solve(content, left=[], right=[], p1=0, p2=0):
    for line in content:
        a, b = [*map(int, line.split('   '))]
        left.append(a)
        right.append(b)

    for a, b in zip(sorted(left), sorted(right)):
        p1 += abs(a - b)
        p2 += right.count(a) * a

    print(p1) # 2430334
    print(p2) # 28786472

if __name__ == "__main__":
    with open('input/day01.txt') as f:
        content = f.read().splitlines()
        solve(content)