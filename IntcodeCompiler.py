def compiler(program, systemID = 0, day2 = False):
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

        # exit condition, with some "debugging" if unexpected opcode
        if opcode not in opcodes:
            if day2: return program[0]
            if opcode == 9 or opcode == 99: return # dont want to see other info
            print('Returned')
            print(opcode)
            print(command)
            print(a,b,c,d,e)
            return

        # get arguments
        args = []
        if opcode == 1 or opcode == 2:
            args = [next(it), next(it), next(it)]
        if opcode == 3 or opcode == 4: 
            args = [next(it)]

        # get positional or immediate
        for i in range(len(args)-1):
            if params[i] == 0: 
                args[i] = program[args[i]]

        try:
            if(opcode == 1):
                program[args[2]] = args[0] + args[1]
            elif opcode == 2:
                program[args[2]] = args[0] * args[1]
            elif opcode == 3:
                program[args[0]] = systemID #input()
            elif opcode == 4:
                print('Out: '+ str(program[args[0]]))
            elif opcode == 5:
                if args[0] != 0:
                    pass
            else:
                exit('Invalid opcode '+ str(opcode))
        except:
            exit('IndexOutOfBounds '+ str(len(program)) +' < '+ str(args[0]) +', '+ str(args[1]) +', '+ str(args[2]))
    
    if day2: return program[0]

if __name__ == '__main__': print('No main in this file.')