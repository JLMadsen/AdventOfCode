from itertools import permutations
import math

def prod_if_sum_equals(e, l, g):
    print([math.prod(p) for p in permutations(e,l) if sum(p)==g][0])

if __name__ == "__main__":
    with open('2020/inputs/day01.txt') as f:
        e = [*map(int, f.read().split('\n')[:-1])]
        prod_if_sum_equals(e, 2, 2020) # part 1: 436404
        prod_if_sum_equals(e, 3, 2020) # part 2: 274879808