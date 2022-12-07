from collections import defaultdict

def solve(content, dirs = defaultdict(lambda: 0), path = ['/']):
    for command in content:
        if '$' in (args := command.split(' ')):
            if args[1] == 'cd':
                if (target := args[2]) == '..': path.pop()
                elif target == '/':             path = ['/']
                else:                           path.append(target)
        elif args[0] == 'dir': continue
        else:
            for i in range(len(path)):
                dirs[str(path[:i+1])[2:-2]] += int(args[0])

    print(sum([v for v in dirs.values() if v <= 1e5])) # 1611443
    print(min([v for v in dirs.values() if v >= dirs['/'] - 4e7])) # 2086088

if __name__ == "__main__":
    with open('input/day07.txt') as f:
        content = f.read().splitlines()
        solve(content)