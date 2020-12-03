import math

def check_tree_encounters(area, slope=(3, 1)):
    return len([0 for i in range(0, len(area), slope[1]) if area[i][((i//slope[1])*slope[0])%len(area[0])]=='#'])

if __name__ == "__main__":
    with open('2020/input/day03.txt') as f:

        data = [[c for c in d] for d in f.read().splitlines()]
        trees = [check_tree_encounters(data, slope) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]

        print(trees[1])         # 252
        print(math.prod(trees)) # 2608962048