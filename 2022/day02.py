moves = ['A', 'B', 'C']
idx     = lambda x: ord(x) - ord('A')
decrypt = lambda _, x: chr(ord(x) - ord('X') + ord('A'))
beats   = lambda a, b: b == moves[ idx(a) - 1 ]
tactic  = lambda x, t: (moves[idx(x) - 2] if t == 'Z' else
                        moves[idx(x) - 1] if t == 'X' else x)

def play(a, b):
    if   beats(a, b): return 0
    elif beats(b, a): return 6
    return 3

def solve(content, b_function, score = 0):
    for hands in content:
        a, b = hands.split()
        b = b_function(a, b)
        score += play(a, b) + idx(b) + 1
    print(score)

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().splitlines()
        solve(content, decrypt) # 15632
        solve(content, tactic) # 14416