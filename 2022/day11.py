from math import prod

def solve(content, pt2 = False, n=7, mod=1, monkeys={}):
    for idx in range(( len(content)//n) +1 ):
        monkey = content[idx*n:idx*n+n]
        mod *= int(monkey[3].split()[-1])
        monkeys[str(idx)] = {'items': [*map(lambda m: int(m.replace(',','')), monkey[1].split()[2:])],
                        'operation': monkey[2].split()[4:], 
                        'test': int(monkey[3].split()[-1]), 
                        'throw_True': monkey[4].split()[-1], 
                        'throw_False': monkey[5].split()[-1], 
                        'count': 0}

    for round in range(20 if not pt2 else 10_000):
        for idx in range(len(monkeys)):
            m = monkeys[str(idx)]
            op, v = m['operation']
            monkeys[str(idx)]['count'] += len(m['items'])

            for item in [*m['items']]:
                new_worry = eval(f'{item}{op}{(v if v != "old" else item)}')
                new_worry = (new_worry // 3) if not pt2 else (new_worry % mod)
                monkeys[m['throw_' + str(new_worry%m['test']==0)]]['items'].append(new_worry)
                monkeys[str(idx)]['items'].remove(item)

    print(prod(sorted([v['count'] for v in monkeys.values()], reverse=True)[:2]))

if __name__ == "__main__":
    with open('input/day11.txt') as f:
        content = f.read().splitlines()
        solve(content) # 99852
        solve(content, True) # 25935263541