# https://adventofcode.com/2019/day/5

def compiler(program):
    opcodes = [1,2,3,4]

    it = iter(range(len(program)))
    for i in it:

        # get opcode and parameter mode
        # turns "01" into "00001"
        command = str(program[i]).split()
        while len(command) != 5:
            command.insert(0,'0')
        command = list(map(int, command))
        a, b, c, d, e = command
        opcode = int(str(d).join(str(e)))
        params = [c,b,a]

        # exit condition
        if opcode not in opcodes:
            print('Returned at index',i)
            print(command)
            return

        # get arguments
        args = []
        if opcode == 1 or opcode == 2:
            args = [next(it), next(it), next(it)]
        if opcode == 3 or opcode == 4: 
            args = [next(it)]

        # get positional or immediate
        for i in range(len(args)):
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