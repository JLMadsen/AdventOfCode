import functools

def compare(a, b):
    a_is_list = isinstance(a, list)
    b_is_list = isinstance(b, list)

    if isinstance(a, int) and isinstance(b, int):
        # (a <= b)
        return 0 if a == b else (-1 if a < b else 1)

    # print(a, b)

    # if a_is_list and b_is_list:
    #     if len(a) < len(b): return 1
    #     if len(a) > len(b): return -1

    if not a_is_list: return compare([a], b)
    if not b_is_list: return compare(a, [b])
    if a and b:
        res = compare(a[0], b[0])
        return res if res else compare(a[1:], b[1:])
        
    return 1 if a else (-1 if b else 0)

    # if a_is_list and not b_is_list:      return compare(a, [b], c)
    # elif b_is_list and not a_is_list:    return compare([a], b, c)
    # elif a_is_list and b_is_list:        return all(compare(x, y, c) for x, y in zip(a, b))

def part1(content):
    correct_packets = []
    previous_packet = ""

    for idx, line in enumerate(content):
        if not line: 
            previous_packet = ""
            continue

        if not previous_packet:
            previous_packet = line
            continue

        packet_a = eval(line)
        packet_b = eval(previous_packet)

        # print()
        # print(packet_a)
        # print(packet_b)

        if compare(packet_b, packet_a) == -1:
            # print('correct')
            correct_packets.append(idx // 3 + 1)

    print(sum(correct_packets)) # 6415

# feil 2102
# feil 2073
# feil 2265
# feil 4862


def part2(content):
    packets = []

    for idx, line in enumerate(content):
        if not line: continue
        packets.append(eval(line))

    packets.append([[2]])
    packets.append([[6]])

    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))
    decoder_key = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
    print(decoder_key) # 20056

ex = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


if __name__ == "__main__":
    with open('input/day13.txt') as f:
        content = f.read().splitlines()
        # content = ex.splitlines()

        part1(content)
        part2(content)