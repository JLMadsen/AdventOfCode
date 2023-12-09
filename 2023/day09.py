def solve(content, pt2=0, value=0):
    for line in map(str.split,content):
        diff = [[*map(int, line)]]

        while not all(n == 0 for n in diff[-1]):
            new_diffs = []
            for a, b in zip(diff[-1], diff[-1][1:]):
                new_diffs.append(int(b)-int(a))
            diff.append(new_diffs)

        for i in range(len(diff)-1, 0, -1):
            if pt2: diff[i-1].insert(0, diff[i-1][0] - diff[i][0])
            else:   diff[i-1].append(diff[i][-1]+diff[i-1][-1])
        value += diff[0][0 if pt2 else -1]

    print(value)

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = f.read().splitlines()
        solve(content)    # 1882395907
        solve(content, 1) # 1005