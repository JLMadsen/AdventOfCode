# https://adventofcode.com/2019/day/5

from IntcodeCompiler import compiler

def main() -> None:
    ints = list(map(int, open('input/day5input.txt').read().split(',')))

    compiler(ints)
    print('done')

if __name__ == '__main__':
    main()