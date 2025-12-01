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

    ffiles = [*files]
    [print( (str(id) if id != -1 else '.') *size, end='') for id, size in ffiles]
    print()

    for id, size in [*files[::-1]]:
        if id == -1:
            continue
        
        for i, (iid, isize) in enumerate(ffiles):
            if iid > 0:
                continue

            if size <= isize:
                # del ffiles[i]
                new_files = [((id, size))]
                if size < isize:
                    new_files.append((iid, isize - size))
                ffiles[i:i + 1] = new_files
                ffiles = [f for f in ffiles if f[0] != id]
                continue
        [print( (str(id) if id != -1 else '.') *size, end='') for id, size in ffiles]
        print()

    # print(ffiles)




t1 = "12345"
t2 = "2333133121414131402"

if __name__ == "__main__":
    with open('input/day09.txt') as f:
        content = f.read().splitlines()
        # part1(content[0])
        # part1(t2)
        # part2(content[0])
        part2(t2)
