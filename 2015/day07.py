from collections import defaultdict

def run(data):

    wires = defaultdict(lambda: 0)

    for instruction in data:

        left, right = instruction.split('->')
        left, right = left.split(' '), right.strip()
        del left[-1]

        if len(left) == 1:
            left = left[0]
            wires[right] = int(left) if left.isnumeric() else wires[left]
        else:
            if 'NOT' in left:
                print('NOT', left, ~(int(left[1]) if left[1].isnumeric() else wires[left[1]]))
                wires[right] = ~(int(left[1]) if left[1].isnumeric() else wires[left[1]])

            elif 'RSHIFT' in left:
                v1, v2 = left[0], left[2]
                v1 = int(v1) if v1.isnumeric() else wires[v1]
                v2 = int(v2) if v2.isnumeric() else wires[v2]
                wires[right] = v1 >> v2

            elif 'LSHIFT' in left:
                v1, v2 = left[0], left[2]
                v1 = int(v1) if v1.isnumeric() else wires[v1]
                v2 = int(v2) if v2.isnumeric() else wires[v2]
                wires[right] = v1 << v2

            elif 'AND' in left:
                v1, v2 = left[0], left[2]
                v1 = int(v1) if v1.isnumeric() else wires[v1]
                v2 = int(v2) if v2.isnumeric() else wires[v2]
                wires[right] = v1 & v2

            elif 'OR' in left:
                v1, v2 = left[0], left[2]
                v1 = int(v1) if v1.isnumeric() else wires[v1]
                v2 = int(v2) if v2.isnumeric() else wires[v2]
                wires[right] = v1 | v2

        print(left, right)

    print(wires)
    print()
    print(wires['a'])


if __name__ == "__main__":
    with open('2015/input/day07.txt') as f:

        data = f.read().splitlines()

        run(data)

