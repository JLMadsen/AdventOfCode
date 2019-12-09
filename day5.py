# https://adventofcode.com/2019/day/5

from IntcodeCompilerWithJump import compiler

def main() -> None:
    program = list(map(int, open('input/day5input.txt').read().split(',')))
    
    program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    compiler(program.copy(), 7)
    compiler(program.copy(), 8)
    compiler(program.copy(), 9)

    #print('Part 1')
    #compiler(program.copy(), 1)

    #print('\nPart 2')
    #compiler(program.copy(), 8)

if __name__ == '__main__':
    main()