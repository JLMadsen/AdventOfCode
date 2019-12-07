# https://adventofcode.com/2019/day/2

from IntcodeCompiler import compiler

def readIntcodesFromFile() -> []:
    
    filename = 'input/day2input.txt'
    program = open(filename).read().split(',')
    
    return list(map(int, program))

def part1() -> int:
    
    program = readIntcodesFromFile()
    
    # replace position 1 with the value 12 
    # replace position 2 with the value 2.
    program[1] = 12
    program[2] = 2
    
    return compiler(program, day2=True)

def part2() -> []:

    ints = readIntcodesFromFile()
    
    # determine what pair of inputs produces the output 19690720
    for a in range(100):
        for b in range(100):
            
            program = ints.copy()
            program[1] = a
            program[2] = b

            if compiler(program, day2=True) == 19690720:
                return [a, b]

def main() -> None:
    print('Day 2')
    print('Task 1:', part1())
    print('Task 2:', part2())
    
if __name__ == '__main__':
    main()