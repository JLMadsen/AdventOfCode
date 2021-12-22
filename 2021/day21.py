from itertools import cycle
from functools import lru_cache

def play_part1(pos_a, pos_b):
    rolls = score_a = score_b = 0
    roll = cycle( range(1, 101) ).__next__

    while 1:
        rolls += 3
        pos_a = (pos_a + roll() + roll() + roll()) 
        pos_a %= 10
        score_a += pos_a + 1
        if score_a >= 1000:
            return score_b * rolls

        rolls += 3
        pos_b = (pos_b + roll() + roll() + roll()) 
        pos_b %= 10
        score_b += pos_b + 1
        if score_b >= 1000:
            return score_a * rolls

"""
when you roll it, the universe splits into multiple copies
one copy for each possible outcome of the die. 
In this case, rolling the die always splits the universe into three copies: 
one where the outcome of the roll was 1, one where it was 2, and one where it was 3.
"""
games = {}

@lru_cache(maxsize=None)
def doctor_strange(pos_a, pos_b, score_a=0, score_b=0):
    global games

    if score_a >= 21:
        return 1, 0
    if score_b >= 21:
        return 0, 1

    res = (0, 0)

    for dice_a in [1, 2, 3]:
        for dice_b in [1, 2, 3]:
            for dice_c in [1, 2, 3]:
                
                alt_pos_a = (pos_a + dice_a + dice_b + dice_c)
                alt_pos_a %= 10
                alt_score_a = score_a + alt_pos_a + 1

                # swap a and b to alternate turns
                a, b = doctor_strange(pos_b, alt_pos_a, score_b, alt_score_a)
                res = (res[0] + b, res[1] + a)
                
    games[(pos_a, pos_b, score_a, score_b)] = res
    return res

with open('input/day21.txt') as f:
    a, b = list(map(lambda n: int(n[-1]) - 1, f.read().split('\n')[:-1]))

    print( play_part1(a, b) ) # 1004670
    print( max(doctor_strange(a, b)) ) # 492043106122795




