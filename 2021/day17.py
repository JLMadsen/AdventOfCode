import re

def simulate(left, right, down, up):
    vecs = set()
    y_max = 0

    for dy in range(-200, 200):
        for dx in range(right + 1):
            vy, vx = dy, dx
            local_y_max = y = x = 0

            while 1:
                x += vx
                y += vy

                if local_y_max < y:
                    local_y_max = y

                if ( left <= x <= right and 
                     down <= y <= up ):

                    vecs.add((dy, dx))
                    y_max = local_y_max if y_max < local_y_max else y_max

                if right < x or y < down:
                    break

                vy -= 1
                vx += (abs(vx)/vx) * -1 if vx != 0 else 0

    print(y_max) # 12561
    print(len(vecs)) # 3785

if __name__ == "__main__":
    with open('input/day17.txt') as f:
        bounds = map(int, re.findall(r'-?\d+', f.read()))
        simulate(*bounds)