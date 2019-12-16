from itertools import permutations
from IntcodeCompiler import Compiler
compiler = Compiler()

def amplify1():
    
    phase_settings = [0,1,2,3,4]
    highest_signal = 0

    perms = list(permutations(phase_settings))
    for perm in perms:
        out = 0
        for setting in perm:

            compiler.loadFilename('input/day7input.txt')
            input = [setting, out]
            program, output = compiler.run(input)
            out = output[-1]

        if out > highest_signal: highest_signal = out

    return highest_signal

def amplify2():
    
    original = compiler.getProgram('input/day7input.txt')
    phase_settings = [5,6,7,8,9]
    highest_signal = 0

    perms = list(permutations(phase_settings))
    for perm in perms:
        instances = [Compiler() for i in perm]

        for instance in instances:
            instance.load(original.copy())

        gens = []
        counter = 0
        while 1:

            counter = counter & len(instances)
            instance = instances[counter]
            








        if out > highest_signal: highest_signal = out

    return highest_signal

def main():
    result = amplify1()
    print('Part 1 =', result)

if __name__ == '__main__':
    main()