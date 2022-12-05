def solve(content, pt2 = False, boxes = []):
    for line in content:
        if '[' in line:
            if not boxes: boxes = [[] for _ in range(len(line)//4+1)]
            for idx, char in enumerate(line[1::4]):
                boxes[idx].insert(0, char) if char != ' ' else None
        elif 'm' in line:
            n, source, dest = map(int, line.split(' ')[1::2])
            n = min(len(boxes[(source := source-1)]), n)
            boxes[dest-1] += boxes[source][-n:][::(1-2*pt2)]
            del boxes[source][-n:]

    print(''.join([stack[-1] for stack in boxes]))

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().splitlines()
        solve(content) # NTWZZWHFV
        solve(content, True) # BRZGFVBTJ