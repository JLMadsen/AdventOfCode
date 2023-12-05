from collections import defaultdict

def solve(content, pt2=0):
    seeds = [*map(int, content[0].split(':')[-1].split())]
    maps = defaultdict(lambda: [])
    current = ""
    for line in content[1:]:
        if 'map' in line:
            current = line.split()[0]
        elif current and line:
            d, s, r = map(int, line.split())
            maps[current].append([s,s+r,d-s])

    locations = []
    low=float('inf')

    def convert(orig):
        number = orig
        for almanac in maps.keys():
            for starts, ends, diffs in maps[almanac]:
                if starts <= number <= ends:
                    number += diffs
                    break
        return number

    if pt2:
        for a, b in [*zip(seeds[::2], seeds[1::2])]:
            for db in range(b):
                number = convert(a+db)
                low=min(low,number)
        print(low - 1)
    else:
        for seed in seeds:
            number = convert(seed)
            locations.append(number)
        print(min(locations))

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().splitlines()
        solve(content) # 3374647
        solve(content, 1) # 6082852