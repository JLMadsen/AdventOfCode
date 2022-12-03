value = lambda char: ord(char.lower()) - ord('a') + 1 + (26 if char.isupper() else 0)

def part1(content, priorities  = 0):
    for line in content:
        a, b = line[:len(line)//2], line[len(line)//2:]
        for c in a:
            if c in b:
                priorities  += value(c)
                break
    print(priorities) # 6256
        
def part2(content, priorities = 0, group = []):
    for line in content:
        group.append(line)
        if len(group) == 3:
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    priorities  += value(c)
                    break
            group = []
    print(priorities) # 2668

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
