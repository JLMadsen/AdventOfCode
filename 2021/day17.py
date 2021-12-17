def simulate(target_area):
    x_target, y_target = target_area
    vecs = set()
    y_max = 0

    for dy in range(-200, 200):
        for dx in range(x_target[1] + 1):
            vy, vx = dy, dx
            local_y_max = y = x = 0

            while 1:
                x += vx
                y += vy

                if local_y_max < y:
                    local_y_max = y

                if ( x_target[0] <= x <= x_target[1] and 
                     y_target[0] <= y <= y_target[1] ):

                    vecs.add((dy, dx))
                    y_max = local_y_max if y_max < local_y_max else y_max

                if x_target[1] < x or y < y_target[0]:
                    break

                vy -= 1
                vx += (abs(vx)/vx) * -1 if vx != 0 else 0

    print(y_max) # 12561
    print(len(vecs)) # 3785

if __name__ == "__main__":
    with open('input/day17.txt') as f:
        content = f.read().strip()[15:].split(',')
        content[1] = content[1].split('=')[1]
        content = [*map(lambda n: [*map(int, n.split('..'))], content)]

        simulate(content)