# https://adventofcode.com/2019/day/5

def compiler(ints):

    it = iter(range(len(ints)))
    for i in it:

        # get opcode and parameter mode
        # turns "01" into "00001"
        command = str(ints[i]).split()
        while len(command) != 5:
            command.insert(0,'0')
        command = list(map(int, command))
        a, b, c, d, e = command
        opcode = e

        if opcode > 4 or opcode < 0:
            return

        # get value, either position or value
        param1, param2 = 0, 0
        if a == 0:
            param1 = ints[ints[i+1]]
        else:
            param1 = ints[i+1]
        if b == 0:
            param2 = ints[ints[i+2]]
        else:
            param2 = ints[i+2]

        param3 = ints[i+3]
        step = 0

        try:
            if(opcode == 1):
                ints[param3] = param1 + param2
                step = 3
            elif opcode == 2:
                ints[param3] = param1 * param2
                step = 3
            elif opcode == 3:
                ints[param1] = 1 #input()
                step = 1
            elif opcode == 4:
                print(ints[param1])
                step = 1
            else:
                exit('Invalid opcode '+ str(opcode))
        except:
            exit('IndexOutOfBounds '+ str(param3))
        
        for j in range(step):
            next(it)

    print(ints)

def main() -> None:
    ints = list(map(int, open('input/day5input.txt').read().split(',')))

    compiler(ints)

if __name__ == '__main__':
    main()