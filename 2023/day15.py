def part1(content):
    value = 0
    for line in content[0].split(','):
        cv = 0
        for char in line:
            cv += ord(char)
            cv *= 17
            cv %= 256
        value += cv
    print(value)

def part2(content):
    value = 0
    boxes = [{} for _ in range(256)]

    def hash(label):
        hash_value = 0
        for char in label:
            hash_value += ord(char)
            hash_value *= 17
            hash_value %= 256
        return hash_value

    for line in content[0].split(','):
        if '=' in line:
            label, focal = line.split('=')
            boxes[hash(label)][label] = int(focal)
        else:
            label = line.split('-')[0]            
            boxes[hash(label)].pop(label, 0)

    for i, box in enumerate(boxes):
        focals = box.values()
        for j, focal in enumerate(focals):
            value += (i + 1)*(j + 1)*(focal)

    print(value)

if __name__ == "__main__":
    with open('input/day15.txt') as f:
        content = f.read().splitlines()
        part1(content) # 516657
        part2(content) # 210906