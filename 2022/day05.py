def solve(content, crateMover = 0, boxes = [], setup = True):
    
    for line in content:
        if not line:
            setup = False
            boxes = [[*reversed(stack)] for stack in boxes]
            continue

        if setup:
            if not boxes:
                boxes = [[] for _ in range(len(line)//4+1)]
            for i in range(0, len(line), 4):
                box = line[i:i+4]
                if '[' not in box: continue
                boxes[i // 4].append(box.strip()[1:-1])
        else:
            _, n, _, source, _, dest = line.split(' ')
            source = int(source) - 1
            dest = int(dest) - 1

            pickup = []
            for i in range(int(n)):
                if len(boxes[source]) == 0:
                    break

                (pickup if crateMover else boxes[dest]).append(boxes[source][-1])
                boxes[source].pop()

            if crateMover:
                boxes[dest] += [*reversed(pickup)]

    print(''.join([stack[-1] for stack in boxes]))

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().splitlines()
        solve(content) # NTWZZWHFV
        solve(content, 1) # BRZGFVBTJ