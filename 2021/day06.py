import time

from collections import defaultdict

def simulate(fish, days=80):
    for _ in range(days):
        for i in range(9):
            fish[i-1] = fish[i]

        fish[8] = fish[-1]
        fish[6] += fish[-1]

    return sum(fish.values()) - fish[-1]
          
if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().split('\n')[:-1]
        fish = defaultdict(lambda: 0)
        [fish.__setitem__(n, fish[n] + 1) for n in [*map(int,content[0].split(','))]]

        print(simulate(fish.copy())) # 383160
        print(simulate(fish, 256)) # 1721148811504
