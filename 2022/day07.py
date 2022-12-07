from collections import defaultdict

def solve2(content, directories = defaultdict(lambda: 0), path = ['/']):
    for command in content:
        if '$' in (args := command.split(' ')):
            if args[1] == 'cd':
                if (target := args[2]) == '..': path.pop()
                elif target == '/':             path = ['/']
                else:                           path.append(target)
        elif args[0] == 'dir': continue
        else:
            for i in range(len(path)):
                directories[str(path[:i+1])] += int(args[0])

    print(sum([value for value in directories.values() # 1611443
        if value <= 100_000]))
        
    print(min([value for value in directories.values() # 2086088
        if value >= directories["['/']"] - (70_000_000 - 30_000_000)]))

if __name__ == "__main__":
    with open('input/day07.txt') as f:
        content = f.read().splitlines()
        solve(content)