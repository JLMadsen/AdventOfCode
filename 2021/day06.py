from collections import defaultdict

def simulate(_fish, days=80):
    fish = defaultdict(lambda: 0)

    for f in _fish:
        fish[f] += 1

    for day in range(days):
        for i in range(9):
            fish[i-1] = fish[i]

        fish[8] = fish[-1]
        fish[6] += fish[-1]

    return sum(fish.values()) - fish[-1]
          
if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().split('\n')[:-1]
        fish = [*map(int,content[0].split(','))]

        print(simulate(fish)) # 383160
        print(simulate(fish, 256)) # 1721148811504