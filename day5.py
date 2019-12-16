# https://adventofcode.com/2019/day/5

from IntcodeCompiler import Compiler
compiler = Compiler()

def main() -> None:
    program = list(map(int, open('input/day5input.txt').read().split(',')))

    compiler.load(program.copy())
    result, output = compiler.run([1])

    print('day 5 part 1', output[-1])

    compiler.load(program.copy())
    result, output = compiler.run([5])

    print('day 5 part 2', output[-1])
    

if __name__ == '__main__':
    main()