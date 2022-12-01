def solve(content):
    elves = [0]
    [elves.__setitem__(-1, elves[-1] + int(cal)) if cal else elves.append(0) for cal in content]
    print(max(elves)) # 68775
    print(sum(sorted(elves, reverse=True)[:3])) # 202585

if __name__ == "__main__":
    with open('input/day01.txt') as f:
        solve(f.read().split('\n')[:-1])