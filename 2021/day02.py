
def get_pos(inst):
    ver = hor = 0
    for line in inst:
        if('down' in line):
            ver += int(line.split()[-1])
        elif('up' in line):
            ver -= int(line.split()[-1])
        elif('forward' in line):
            hor += int(line.split()[-1])
    return ver * hor


def get_pos2(inst):
    aim = hor = depth = 0
    for line in inst:
        if('down' in line):
            aim += int(line.split()[-1])
        elif('up' in line):
            aim -= int(line.split()[-1])
        elif('forward' in line):
            hor += int(line.split()[-1])
            depth += aim * int(line.split()[-1])
    return depth * hor


if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().split('\n')[:-1]

        print(get_pos(content))
        print(get_pos2(content))
