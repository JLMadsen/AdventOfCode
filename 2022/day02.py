moves = ['A', 'B', 'C']
idx = lambda x: ord(x) - ord('A')
decrypt = lambda x: chr(ord(x) - ord('X') + ord('A'))
beats = lambda a, b: b == moves[ idx(a) - 1 ]

def play(a, b):
    if beats(a, b):   return 0
    elif beats(b, a): return 6
    return 3

def part1(content):
    score = 0
    for hands in content:
        a, b = hands.split()
        b = decrypt(b)
        score += play(a, b) + idx(b) + 1
    print(score)

def part2(content):
    score = 0
    for hands in content:
        a, tactic = hands.split()
        b = (moves[(idx(a) + 1) % len(moves)] if tactic == 'Z' else
             a if tactic == 'Y' else
             moves[ idx(a) - 1 ])
        score += play(a, b) + idx(b) + 1
    print(score)

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().splitlines()
        part1(content) # 15632
        part2(content) # 14416