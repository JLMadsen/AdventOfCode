from itertools import product

def solve(content, p2=False, value=0):
    for line in content:
        target, numbers = line.split(':')
        numbers = [*map(int,numbers.split())]
        ops = '*+' if not p2 else '*+|'
        for perm in product(ops, repeat=(len(numbers) - 1)):
            sum = numbers[0]
            
            for number, op in zip(numbers[1:], "".join(perm)):
                if op == '*':
                    sum *= number
                elif op == '+':
                    sum += number
                else:
                    sum = int( str(sum) + str(number) )

            if sum == int(target):
                value += int(target)
                break

    print(value)
        # 28730327770375
        # 424977609625985

if __name__ == "__main__":
    with open('input/day07.txt') as f:
        content = f.read().splitlines()
        solve(content)
        solve(content, True)