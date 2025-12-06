nth = lambda arr, n: [*zip(*arr)][n]

def part1(content):
    value = 0
    problems = [[] for _ in content]

    for i, line in enumerate(content):
        buffer = ''
        for char in line + ' ':
            if char == ' ':
                if buffer != '':
                    problems[i].append(buffer)
                    buffer = ''
            else:
                buffer += char
        
    for problem in [nth(problems, i) for i in range(len(problems[0]))]:
        value += eval( problem[-1].join(problem[:-1]) )

    print(value)

def part2(content):
    value = 0
    numbers = []
    operand = ''
    content = [line + ' ' for line in content] # to trigger the all == ' ' check

    for index in range(len(content[0])):
        line = nth(content, index)

        if line[-1] != ' ':
            operand = line[-1]

        if all(char == ' ' for char in line):
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
