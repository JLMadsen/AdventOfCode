def lift(content):
    value = 0
    new_grid = [[*line] for line in content]
    
    for y in range(len(content)):
        for x in range(len(content[0])):
            neighbours = 0

            for dy, dx in [(y+i, x+j) for i in range(-1,1 + 1) for j in range(-1,1 + 1)]:
                if dy < 0 or dy >= len(content) or dx < 0 or dx >= len(content[0]):
                    continue

                neighbours += content[dy][dx] == '@'

            if content[y][x] == '@' and neighbours < 5:
                new_grid[y][x] = '.'
                value += 1
    
    return (value, new_grid)

def part1(content):
    print(lift(content)[0])

def part2(content):
    value = 0

    while 1:
        removed, content = lift(content)
        value += removed

        if not removed:
            break

    print(value)
    
if __name__ == "__main__":
    with open('input/day04.txt') as f:
        content = f.read().splitlines()
        part1(content) # 1346
        part2(content) # 8493
