import re
nth = lambda arr, n: [*zip(*arr)][n]

def part1(content, value = 0, problems = []):

    for line in content[:-1]:
        problems.append(re.findall(r'\d+', line))
    
    ops = content[-1].replace(' ', '')

    for i in range(len(problems[0])):
        numbers = nth(problems, i)
        value += eval(ops[i].join(numbers))

    print(value)

def part2(content, value = 0, numbers = [], operand = ''):
    content = [line + ' ' for line in content] # to trigger the last space check

    for index in range(len(content[0])):
        line = nth(content, index)

        if not line[-1].isspace():
            operand = line[-1]

        if all(char.isspace() for char in line):
            value += eval(operand.join(numbers))
            numbers = []
        else:
            numbers.append(''.join(line[:-1]))

    print(value)    
    
if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().splitlines()
        part1(content) # 5784380717354
        part2(content) # 7996218225744
