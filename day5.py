# https://adventofcode.com/2019/day/5

from IntcodeCompilerWithJump import compiler

def main() -> None:
    program = list(map(int, open('input/day5input.txt').read().split(',')))

    print('Part 1')
    compiler(program.copy(), 1)

    print('Part 2')
    compiler(program.copy(), 10)

if __name__ == '__main__':
    main()