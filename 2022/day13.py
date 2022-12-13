import functools

def compare(a, b, *_):
    if isinstance(a, int) and isinstance(b, int):
        return (1-2*(a<b))*(a!=b)

    if not isinstance(a, list): return compare([a], b)
    if not isinstance(b, list): return compare(a, [b])
    if a and b:
        res = compare(a[0], b[0])
        return res if res else compare(a[1:], b[1:])
        
    return 1 if a else (-1 if b else 0)

def part1(content, value = 0):
    for i in range(0, len(content), 3):
        if compare(*map(eval, content[i:i+3][:2])) == -1:
            value += i//3+1

    print(value)

def part2(content):
    packets = [eval(line) for line in content if line]
    packets.append([[2]])
    packets.append([[6]])

    # https://stackoverflow.com/questions/16362744
    packets = sorted(packets, key=functools.cmp_to_key(compare))
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))

if __name__ == "__main__":
    with open('input/day13.txt') as f:
        content = f.read().splitlines()
        part1(content) # 6415
        part2(content) # 20056