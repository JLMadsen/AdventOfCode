opening    = ['(', '[', '{', '<']
closing    = [')', ']', '}', '>']
score      = [3, 57, 1197, 25137]
incomplete = []

def get_stack(line):
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        else:
            if char != closing[ opening.index( stack.pop() ) ]:
                return char
    incomplete.append(stack)

def parse(lines):
    error = [ char for line in lines if (char:=get_stack(line)) ]
    return sum([ score[idx] * error.count(char) for idx, char in enumerate(closing)])

def finish_lines():
    points = []
    for stack in incomplete:
        points.append(0)
        for char in reversed(stack):
            points[-1] = points[-1] * 5 + opening.index(char) + 1

    return sorted(points)[ (len(points) -1 ) // 2 ]

if __name__ == "__main__":
    with open('input/day10.txt') as f:
        content = f.read().split('\n')[:-1]
        
        print(parse(content)) # 436497
        print(finish_lines()) # 2377613374
