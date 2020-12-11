

def overlap(moves):
    seen = set()

    x = y = 0

    for move in moves:
        if '>' in move:
            x += 1
        elif '<' in move:
            x -= 1
        elif 'v' in move:
            y += 1
        elif '^' in move:
            y -= 1

        seen.add((x, y))

    print(len(seen))

def overlap_with_robo_santa(moves):
    seen = set()

    x1 = y1 = 0
    x2 = y2 = 0

    for i, move in enumerate(moves):
        if i&1:
            if '>' in move:
                x1 += 1
            elif '<' in move:
                x1 -= 1
            elif 'v' in move:
                y1 += 1
            elif '^' in move:
                y1 -= 1
        else:
            if '>' in move:
                x2 += 1
            elif '<' in move:
                x2 -= 1
            elif 'v' in move:
                y2 += 1
            elif '^' in move:
                y2 -= 1

        seen.add((x1, y1))
        seen.add((x2, y2))
        
    print(len(seen))


if __name__ == "__main__":
    with open('2015/input/day03.txt') as f:

        data = f.read()

        overlap(data) # < 7104
        overlap_with_robo_santa(data)
