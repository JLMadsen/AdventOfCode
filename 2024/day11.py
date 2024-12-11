from collections import defaultdict

def solve(content, blinks):
    stones = defaultdict(lambda: 0)
    for n in [*map(int, content.split())]:
        stones[n] += 1

    for _ in range(blinks):
        new_stones = defaultdict(lambda: 0)
        for key, value in stones.items():
            str_stone = str(key)
            if key == 0:
                new_stones[1] += value
            elif len(str_stone) % 2 == 0:
                new_stones[int(str_stone[:len(str_stone)//2])] += value
                new_stones[int(str_stone[len(str_stone)//2:])] += value
            else:
                new_stones[key * 2024] += value
        stones = new_stones
    print(sum(v for v in stones.values()))

if __name__ == "__main__":
    with open('input/day11.txt') as f:
        content = f.read().splitlines()
        solve(content[0], 25)
        solve(content[0], 75)