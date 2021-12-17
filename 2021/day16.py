import math

hex_to_bin = lambda x: bin(int(x, 16))[2:]
hex_to_bin2 = lambda x: bin(int('1' + x, 16))[3:]

ops = [ sum, 
        math.prod,
        min, 
        max, 
        None,
        lambda x: int(x[0] >  x[1]),
        lambda x: int(x[0] <  x[1]),
        lambda x: int(x[0] == x[1]) ]

def parse(data):
    pos = 0
    version = 0

    def read_int(n):
        nonlocal pos
        result = data[pos: pos+n]
        pos += n
        return int(result, 2)

    def read_packet():
        nonlocal pos
        nonlocal version

        version += read_int(3)
        type_id = read_int(3)

        if type_id == 4:
            value = 0
            while 1:
                last = read_int(1) == 0
                value = (value << 4) + read_int(4)
                if last: 
                    return value

        numbers = []
        length_type = read_int(1)

        if length_type == 0:
            target = pos + read_int(15)
            while pos < target:
                numbers.append( read_packet() )

        else:
            subpackets = read_int(11)
            for _ in range(subpackets):
                numbers.append( read_packet() )

        return ops[type_id](numbers)

    return read_packet(), version

if __name__ == "__main__":
    with open('input/day16.txt') as f:
        content = f.read().strip()

        result, version = parse( hex_to_bin2(content) )

        print(version) # 977
        print(result) # 101501020883