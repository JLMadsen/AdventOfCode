d = {'D': (-1, 0), 'L': (0,-1), 'U': (1, 0), 'R': (0,1)}

def solve(content, length = 2):
    segments = [(0,0) for _ in range(length)]
    visited = set([(0,0)])

    for line in content:
        direction, speed = line.split(' ')
        delta = d[direction]

        for _ in range(int(speed)):
            head = segments[0]
            segments[0] = (head[0] + delta[0], head[1] + delta[1])

            for i in range(len(segments)-1):
                (hx, hy), (tx, ty) = segments[i:i+2]

                dx = abs(hx-tx)
                dy = abs(hy-ty)

                diag = (hx!=tx and  hy!=ty and (dx > 1 or dy > 1))

                if dx > 1 or diag:
                    tx += 1 if hx>tx else -1

                if dy > 1 or diag:
                    ty += 1 if hy>ty else -1

                segments[i+1] = (tx, ty)

                if i ==  len(segments) - 2:
                    visited.add((tx, ty))

    print(len(visited))

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = f.read().splitlines()
        solve(content) # 6026
        solve(content, 10) # 2273