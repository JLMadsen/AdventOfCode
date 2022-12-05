def solve(content, createMover9000 = 0):
    boxes = []
    setup = True

    for line in content:
        if line == '':
            setup = False
            boxes = [[*reversed(stack)] for stack in boxes]
            continue

        if setup:
            layer = []
            if len(boxes) == 0:
                boxes = [[] for _ in range(len(line)//4+1)]
            for i in range(0, len(line), 4):
                box = line[i:i+4]
                if '[' not in box:
                    continue
                idx = i // 4 + 1
                boxes[idx-1].append(box.strip()[1:-1])
        else:
            _, n, _, source, _, destination = line.split(' ')
            n = int(n)
            source = int(source)-1
            destination = int(destination)-1

            pickup = []
            for i in range(n):
                if len(boxes[source]) == 0:
                    break

                if createMover9000:
                    pickup.append(boxes[source][-1])
                else:
                    boxes[destination].append(boxes[source][-1])
                boxes[source].pop()

            if createMover9000:
                boxes[destination] += [*reversed(pickup)]

    result = ''
    for stack in boxes:
        result += stack[-1]
    print(result)

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().splitlines()
        solve(content) # NTWZZWHFV
        solve(content, 1) # BRZGFVBTJ
