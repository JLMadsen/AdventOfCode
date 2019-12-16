from IntcodeCompiler import Compiler

def getProg(filename):
    return list(map(int, open(filename).read().split(',')))

def Test():

    compiler = Compiler()

    day2 = getProg('input/day2input.txt')
    day5 = getProg('input/day5input.txt')
    day9 = getProg('input/day9input.txt')
    comparator = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    #_______________________________ day 2
    day2[1], day2[2] = 12, 2
    compiler.load(day2.copy())
    result, output = compiler.run()

    assert result[0] == 3562624, 'Day 2 failed'

    #_______________________________ day 5.1
    input = [1]
    compiler.load(day5.copy())
    result, output = compiler.run(input)

    assert output[-1] == 16434972, 'Day 5 part 1 failed'

    #_______________________________ day 5.2
    input = [5]
    compiler.load(day5.copy())
    result, output = compiler.run(input)
    
    assert output[-1] == 16694270, 'Day 5 part 2 failed'

    #_______________________________ Comparator
    less = [7]
    equals = [8]
    greater = [9]

    compiler.load(comparator.copy())
    result, output = compiler.run(less)

    assert output[-1] == 999, 'Comparator less failed'

    compiler.load(comparator.copy())
    result, output = compiler.run(equals)

    assert output[-1] == 1000, 'Comparator equals failed'

    compiler.load(comparator.copy())
    result, output = compiler.run(greater)

    assert output[-1] == 1001, 'Comparator greater failed'

    #_______________________________ Day 9
    compiler.load(day9)
    result, output = compiler.run([1])
    print(output)


    #_______________________________ Finished
    import re
    tests = len(re.findall(r'assert', open('IntcodeCompilerTest.py').read()))
    print('Ran', tests,'tests.\nAll passed')


if __name__ == '__main__':
    Test()