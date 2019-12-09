def compiler(program, systemID = 0, day2 = False):
    print('Start program')
    opcodes = [1,2,3,4,5,6,7,8]

    # instruction register
    ir = 0
    
    while True:
        # get opcode and parameter mode
        # turns "01" into "00001"
        command = list(map(int, str(program[ir])))
        a,b,c,d,e = 0,0,0,0,0
        if len(command) == 5: a = command[-5]
        if len(command) >= 4: b = command[-4]
        if len(command) >= 3: c = command[-3]
        if len(command) >= 2: d = command[-2]
        if len(command) >= 1: e = command[-1]

        opcode = int(str(d)+str(e))
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
        length = [[3,4],[5,6],[1,2,7,8]]
        for i in range(len(length)):
            if opcode in length[i]:
                for j in range(i+1):
                    args.append(program[ir+1+j])

        # get positional or immediate
        foo = len(args)-1 if not opcode in length[1] else len(args)
        for i in range(foo):
            if params[i] == 0: 
                args[i] = program[args[i]]

        #print('\nprog', program)
        #print('code', ir, params, opcode, args)
        #if opcode == 3: print('input', systemID)

        jump = False
        try:
            # add
            if(opcode == 1):
                program[args[2]] = args[0] + args[1]
            # mupltiply
            elif opcode == 2:
                program[args[2]] = args[0] * args[1]
            # input
            elif opcode == 3:
                program[args[0]] = systemID #input()
            # print
            elif opcode == 4:
                print('Out: '+ str(args[0]))
            # jump if true
            elif opcode == 5:
                if args[0] != 0:
                    jump = True
                    ir = args[1]
            # jump if false
            elif opcode == 6:
                if args[0] == 0:
                    jump = True
                    ir = args[1]
            # less than
            elif opcode == 7:
                program[args[2]] = 1 if args[0] < args[1] else 0   
            # equals 
            elif opcode == 8:
                program[args[2]] = 1 if args[0] == args[1] else 0
            else:
                print(args, flush=True)
                exit('Invalid opcode '+ str(opcode))
        except:
            print(args, flush=True)
            exit('IndexOutOfBounds '+ str(opcode))

        #print('prog', program,'\n')
        
        if not jump:
            ir += len(args)+1
    
    if day2: return program[0]

if __name__ == '__main__': print('No main in this file.')