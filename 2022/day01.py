def solve(content):
    elfs = [0]
    for cal in content:
        if not cal: elfs.append(0)
        else: elfs[-1] += int(cal)

    print(max(elfs)) # 68775
    print(sum(sorted(elfs, reverse=True)[:3])) # 202585

if __name__ == "__main__":
    with open('input/day01.txt') as f:
        solve(f.read().split('\n')[:-1])