d = {'D': (-1, 0), 'L': (0,-1), 'U': (1, 0), 'R': (0,1)}
taxicab = lambda hx,hy,tx,ty: abs(tx-hx) + abs(ty-hx)
n,m=26,26

def print_grid(hx, hy, tx, ty):
    for y in range(n):
        for x in range(m):
            s = '.'
            s = 'T' if hx == x and hy == y else s
            s = 'H' if tx == x and ty == y else s
            print(s,end="")
        print()
    print()

def part1(content):
    tx, ty = 0,0
    hx, hy = 0,0
    visited = set()
    visited.add((tx, ty))

    for line in content:
        direction, speed = line.split(' ')
        delta = d[direction]
        # print_grid(hx, hy,tx, ty)

        for _ in range(int(speed)):
            hx, hy = hx + (delta[1]), hy + (delta[0])
            dx = abs(hx-tx)
            dy = abs(hy-ty)

            diag = (hx!=tx and  hy!=ty and (dx > 1 or dy > 1))

            if dx > 1 or diag:
                tx += 1 if hx>tx else -1

            if dy > 1 or diag:
                ty += 1 if hy>ty else -1

            # print(hx, hy, '>',tx, ty,'','',dx,dy,(dx>1 or dy>1))

            visited.add((tx, ty))
            # print_grid(hx, hy,tx, ty)

    print(len(visited))
# feil 261
# feil 38
# feil 5907
# feil 5908

def part2(content):
    segments = [(0,0) for _ in range(10)]
    visited = set()
    visited.add((0, 0))

    for line in content:
        direction, speed = line.split(' ')
        delta = d[direction]

        for _ in range(int(speed)):
            head = segments[0]
            segments[0] = (head[0]+ (delta[1]), head[1]+ (delta[0]))

            for i in range(len(segments)-1):
                a, b = segments[i:i+2]
                hx, hy = a
                tx, ty = b

                dx = abs(hx-tx)
                dy = abs(hy-ty)

                diag = (hx!=tx and  hy!=ty and (dx > 1 or dy > 1))

                if dx > 1 or diag:
                    tx += 1 if hx>tx else -1

                if dy > 1 or diag:
                    ty += 1 if hy>ty else -1

                segments[i+1] = (tx, ty)

                visited.add((tx, ty)) if i == 8 else None

    print(len(visited))

ex = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
