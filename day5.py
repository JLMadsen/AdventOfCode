# https://adventofcode.com/2019/day/5

def compiler(program):
    opcodes = [1,2,3,4]

    it = iter(program)
    for i in it:

        # get opcode and parameter mode
        # turns "01" into "00001"
        command = list(map(int, str(i)))
        a,b,c,d,e = 0,0,0,0,0

        if len(command) == 5: a = command[-5]
        if len(command) >= 4: b = command[-4]
        if len(command) >= 3: c = command[-3]
        if len(command) >= 2: d = command[-2]
        if len(command) >= 1: e = command[-1]

        opcode = int(str(d).join(str(e)))
        params = [c,b,a]

        # exit condition
        if opcode not in opcodes:
            print('Returned',opcode)
            print(command)
            print(a,b,c,d,e)
            return

        # get arguments
        args = []
        if opcode == 1 or opcode == 2:
            args = [next(it), next(it), next(it)]
        if opcode == 3 or opcode == 4: 
            args = [next(it)]

        print(params, opcode, args)

        # get positional or immediate
        for i in range(len(args)-1):
            if params[i] == 0: 
                args[i] = program[args[i]]

        print(params, opcode, args)

        try:
            if(opcode == 1):
                program[args[2]] = args[0] + args[1]
            elif opcode == 2:
                program[args[2]] = args[0] * args[1]
            elif opcode == 3:
                program[args[0]] = 1 #input()
            elif opcode == 4:
                print('Out: '+ str(program[args[0]]))
            else:
                exit('Invalid opcode '+ str(opcode))
        except:
            exit('IndexOutOfBounds '+ str(len(program)) +' < '+ str(args[0]) +', '+ str(args[1]) +', '+ str(args[2]))           

    print(program)

def main() -> None:
    ints = list(map(int, open('input/day5input.txt').read().split(',')))

    compiler(ints)
    print('done')

if __name__ == '__main__':
    main()