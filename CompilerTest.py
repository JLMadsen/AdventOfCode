from IntcodeCompiler import Compiler

def getProg(filename):
    return list(map(int, open(filename).read().split(',')))

def Test():

    compiler = Compiler()

    day2 = getProg('input/day2input.txt')
    day5 = getProg('input/day5input.txt')
    comparator = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    #_______________________________ day 2
    day2[1], day2[2] = 12, 2
    compiler.load(day2.copy())
    result, output = compiler.run()

    if (res := result[0]) == 3562624:
        print('Day 2 passed')
    else:
        print('Day 2 failed,', res)

    #_______________________________ day 5.1
    input = [1]
    compiler.load(day5.copy())
    result, output = compiler.run(input)

    if (res := output[-1]) == 16434972:
        print('Day 5 part 1 passed')
    else:
        print('Day 5 part 2 failed,', res)

    #_______________________________ day 5.2
    input = [5]
    compiler.load(day5.copy())
    result, output = compiler.run(input)
    
    if (res := output[-1]) == 16694270:
        print('Day 5 part 2 passed')
    else:
        print('Day 5 part 2 failed', res)

    #_______________________________ Comparator
    less = [7]
    equals = [8]
    greater = [9]

    compiler.load(comparator.copy())
    result, output = compiler.run(less)

    if (res := output[-1]) == 999:
        print('Comparator less passed')
    else:
        print('Comparator less failed', res)

    compiler.load(comparator.copy())
    result, output = compiler.run(equals)

    if (res := output[-1]) == 1000:
        print('Comparator equals passed')
    else:
        print('Comparator equals failed', res)

    compiler.load(comparator.copy())
    result, output = compiler.run(greater)

    if (res := output[-1]) == 1001:
        print('Comparator greater passed')
    else:
        print('Comparator greater failed', res)



if __name__ == '__main__':
    Test()