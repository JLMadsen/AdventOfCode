value = lambda char: ord(char.lower()) - ord('a') + 1 + (26 if char.isupper() else 0)

def part1(content, priorities = 0):
    for line in content:
        a, b = line[:len(line)//2], line[len(line)//2:]
        priorities += [value(c) for c in a if c in b][0]
    print(priorities) # 6256
        
def part2(content, priorities = 0):
    for i in range(0, len(content), 3):
        priorities += value(set.intersection(*map(set, content[i:i+3])).pop())
    print(priorities) # 2668

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)