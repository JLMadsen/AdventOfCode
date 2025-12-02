def part1(content, value = 0):
    
    for line in content:
        a, b = map(int, line.split('-'))

        for id in range(a, b + 1):
            id = str(id)
            middle = len(id) // 2
            if id[:middle] == id[middle:]:
                value += int(id)

    print(value)

def part2(content, value = 0):
    
    for line in content:
        a, b = map(int, line.split('-'))

        for id in range(a, b + 1):
            id = str(id)

            for length in range(1, (len(id)//2 + 1)):
                for index in range(0, len(id), length):
                    if id[index: index + length] != id[:length]:
                        break
                else:
                    value += int(id)
                    break

    print(value)

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().split(',')
        part1(content) # 31210613313
        part2(content) # 41823587546
