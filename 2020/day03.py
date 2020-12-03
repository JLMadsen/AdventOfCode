import math

def check_tree_encounters(area, slope=(3, 1)):
    return len([0 for i,l in enumerate(area) if not i%slope[1] and l[(i*slope[0])%len(area[0])]=='#'])

def check_tree_encounters_old(area, slope):
    trees = 0
    x = y = 0

    while 1:
        x += slope[0]
        y += slope[1]

        try:
            trees += 1 if area[y][(x%len(area[0]))] == '#' else 0
        except:
            break

    return trees

if __name__ == "__main__":
    with open('2020/input/day03.txt') as f:

        data = f.read().splitlines() 
        data = [[c for c in d] for d in data]

        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees = [check_tree_encounters(data, slope) for slope in slopes]

        print(trees[1])         # 252
        print(math.prod(trees)) # 2608962048