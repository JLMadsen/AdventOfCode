def part1(content):
    files = []

    for i, n in enumerate(content):
        if i % 2 == 0:
            files += [i // 2] * int(n)
        else:
            files += ['.'] * int(n)

    # print(''.join(map(str,files)))
    while any(
        a == '.' and b != '.'
        for a, b in zip(files, files[1:])
    ):
        block = '.'
        while block == '.':
            block = files[-1]
            files = files[:-1]

        index = files.index('.')
        files[index:index + 1] = [block]
        # print(''.join(map(str,files)))
    # print(''.join(map(str,files)))

    print(sum(
        i * int(n)
        for i, n in
        enumerate(files)
        if n != '.'
    )) # 6370402949053

def part2(content):
    files = []

    for i, n in enumerate(content):
        if i % 2 == 0:
            files.append((i//2, int(n)))
        else:
            files.append((-1, int(n)))

    # print(''.join(map(str,files)))
    while 1:
        block = (-1, 0)
        while block[0] == -1:
            block = files.pop()
            # files = files[:-1]
        b_id, b_size = block

        for index, f in enumerate(files):
            id, size = f
            if id >= 0:
                continue
            if size <= b_size:
                files[index:index + 1] = [(-1, size-b_size)]
                files[index:index] = [block]
                break

        for i,v in files:
            if i < 0:
                print('.' * v, end='')
            else:
                print(str(i) * v, end='')
        print(block)

    #     print(''.join(map(str,files)))
    # print(''.join(map(str,files)))

    # print(sum(
    #     i * int(n)
    #     for i, n in
    #     enumerate(files)
    #     if n != '.'
    # )) # 6370402949053

t1 = "12345"
t2 = "2333133121414131402"

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = f.read().splitlines()
        # part1(content[0])
        part1(t2)
        # part2(content[0])
        part2(t2)
