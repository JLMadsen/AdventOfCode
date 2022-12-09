d = {'D':(-1,0),'U':(1,0),'L':(0,-1),'R':(0,1)}

def solve(content, length = 2, visited = set()):
    rope = [(0,0)] * length

    for line in content:
        direction, speed = line.split()
        mod = d[direction]

        for _ in range(int(speed)):
            rope[0] = (rope[0][0] + mod[0], 
                       rope[0][1] + mod[1])

            for i in range(len(rope)-1):
                (hx, hy), (tx, ty) = rope[i:i+2]
                dx, dy = abs(hx-tx), abs(hy-ty)

                diag = hx!=tx and hy!=ty and (dx > 1 or dy > 1)

                if dx > 1 or diag: tx += 1-2*(hx<tx)
                if dy > 1 or diag: ty += 1-2*(hy<ty)
                
                rope[i+1] = (tx, ty)
                if i == len(rope) - 2:
                    visited.add((tx, ty))

    print(len(visited))

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = f.read().splitlines()
        solve(content) # 6026
        solve(content, 10) # 2273