from itertools import permutations
import get_input
import math

def prod_if_sum_equals(e, l, g):
    print([math.prod(p) for p in permutations(e,l) if sum(p)==g][0])

if __name__ == "__main__":
    with open('2020/input/day01.txt') as f:
        e = [*map(int, f.readlines())]
        prod_if_sum_equals(e, 2, 2020) # 436404
        prod_if_sum_equals(e, 3, 2020) # 274879808