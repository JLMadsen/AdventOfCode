def solve(content):
    elves = [0]
    for cal in content:
        if not cal: elves.append(0)
        else: elves[-1] += int(cal)

    print(max(elves)) # 68775
    print(sum(sorted(elves, reverse=True)[:3])) # 202585

if __name__ == "__main__":
    with open('input/day01.txt') as f:
        solve(f.read().split('\n')[:-1])