from collections import defaultdict

def solve(content):
    directories = defaultdict(lambda: 0)
    path = ['/']

    for command in content:
        args = command.split(' ')

        if '$' in args:
            if args[1] == 'cd':
                target = args[2]
                if target == '..':  path.pop()
                elif target == '/': path = ['/']
                else:               path.append(target)

        else:
            if args[0] == 'dir': continue
            size, filename = args
            directories[''.join(path)] += int(size)

            for idx in range(1, len(path)):
                tmp_path = ''.join(path[:-idx])
                directories[tmp_path] += int(size)

    value = 0
    for d, v in directories.items():
        if v <= 100_000:
            value += v

    print(value) # 1611443

    min_dir_size = float('inf')
    total = directories['/'] - 40_000_000
    for d, v in directories.items():
        if v >= total and v < min_dir_size:
            min_dir_size = v
            
    print(min_dir_size) # 2086088

if __name__ == "__main__":
    with open('input/day07.txt') as f:
        content = f.read().splitlines()
        solve(content)