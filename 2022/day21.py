def solve(content, pt2 = False, monkeys = {}):
    for line in content:
        monke, eq = line.split(':')
        if eq.strip().isdigit(): monkeys[monke] = int(eq)
        else:                    monkeys[monke] = eq
    monkeys_copy = monkeys.copy()

    def yell(pt2 = False):
        while not all(isinstance(value, int) for value in monkeys.values()):
            for monkey, value in monkeys.items():
                if isinstance(value, str):
                    a, op, b = value.split()
                    if (isinstance(monkeys[a], int) and 
                        isinstance(monkeys[b], int)):
                        monkeys[monkey] = int(eval(f"{monkeys[a]}{op}{monkeys[b]}"))
                        if monkey == "root" and pt2:
                            return monkeys[a] - monkeys[b]

    yell()
    print(( root := monkeys["root"])) # 66174565793494
    monkeys = monkeys_copy.copy()

    def setHumnAndCopyMonkeys(n):
        nonlocal monkeys
        monkeys = monkeys_copy.copy()
        monkeys['humn'] = n

    v1, v2 = 0, 100
    setHumnAndCopyMonkeys(v1); d1 = yell(True)
    setHumnAndCopyMonkeys(v2); d2 = yell(True)

    while 1:
        if abs(d1) < abs(d2):
            v2 = v1 - ( v2 - v1 ) * d1 / (d2 - d1)
            setHumnAndCopyMonkeys(int(v2))
            d2 = yell(True)
            if d2 == 0: print(int(v2) - 1); break
        else:
            v1 = v2 - ( v1 - v2 ) * d2 / (d1 - d2)
            setHumnAndCopyMonkeys(int(v1))
            d1 = yell(True)
            if d1 == 0: print(int(v1) - 1); break

        # 3327575724809

if __name__ == "__main__":
    with open('input/day21.txt') as f:
        content = f.read().splitlines()
        solve(content) 