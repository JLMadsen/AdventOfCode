# TO BE REFACTORED

scores = {'X': 1, 'Y': 2, 'Z': 3}

shape = {'A': 'X',
         'B': 'Y',
         'C': 'Z',
         'X': 'A',
         'Y': 'B',
         'Z': 'C'}

beats = {'X': 'Z',
         'Y': 'X',
         'Z': 'Y'}

def play(hand_a, hand_b, a_beats, b_beats):
        if b_beats == hand_a:                
            return 6
        elif b_beats != hand_a and a_beats != hand_b:  
            return 3
        else:                       
            return 0

def part1(content):
    score = 0
    for hands in content:
        a, b = hands.split()
        ax = shape[a]
        ay = beats[ax]
        by = beats[b]

        score += play(ax, b, ay, by) + scores[b]

    print(score) # 15632

def part2(content):
    score = 0
    for hands in content:
        a, tactic = hands.split()
        ax = shape[a]
        ay = beats[ax]
        bx = [k for k, v in beats.items() if v == ax][0]

        b = ''
        if tactic == 'X':   b = ay
        elif tactic == 'Y': b = ax
        else:               b = bx

        by = beats[b]

        score += play(ax, b, ay, by) + scores[b]

    print(score) # 14416

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)