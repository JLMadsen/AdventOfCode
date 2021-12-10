opening_brackets = ['(', '[', '{', '<']
closing_brackets = [')', ']', '}', '>']
score            = [3, 57, 1197, 25137]
incomplete_lines = []

def get_stack(line):
    global incomplete_lines
    stack = []
    for char in line:
        if char in opening_brackets:
            stack.append(char)
        else:
            last = stack.pop()
            idx = closing_brackets.index(char)
            expected = closing_brackets[ opening_brackets.index(last) ]
            if char != expected:
                return char
    incomplete_lines.append(stack)

def parse(lines):
    error = []

    for line in lines:
        if (char:=get_stack(line)):
            error.append(char)
    
    points = 0
    for idx, char in enumerate(closing_brackets):
        points += score[idx] * error.count(char)

    return points

def finish_lines():
    global incomplete_lines
    points = []
    for stack in incomplete_lines:
        
        points.append(0)
        for char in reversed(stack):
            points[-1] = points[-1] * 5 + opening_brackets.index(char) + 1

    points = sorted(points)
    return points[ (len(points) -1 )// 2 ]

if __name__ == "__main__":
    with open('input/day10.txt') as f:
        content = f.read().split('\n')[:-1]
        
        print(parse(content)) # 436497
        print(finish_lines()) # 2377613374
