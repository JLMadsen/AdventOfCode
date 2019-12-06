# https://adventofcode.com/2019/day/2

def IntcodeCompiler(ints) -> int:

    for i in range(0, len(ints), 4):
        opcode = ints[i]
        addr1 = ints[i+1]
        addr2 = ints[i+2]
        addr3 = ints[i+3]

        try:
            if opcode == 99:
                return ints[0]
            elif opcode == 1:
                ints[addr3] = ints[addr1] + ints[addr2]
            else:
                ints[addr3] = ints[addr1] * ints[addr2]
        except:
            # IndexOutOfBounds
            return 0

def readIntcodesFromFile() -> []:
    
    filename = 'input/day2input.txt'
    ints = open(filename).read().split(',')
    
    return list(map(int, ints))

def part1() -> int:
    
    ints = readIntcodesFromFile()
    
    # replace position 1 with the value 12 
    # replace position 2 with the value 2.
    ints[1] = 12
    ints[2] = 2
    
    return IntcodeCompiler(ints)

def part2() -> []:

    ints = readIntcodesFromFile()
    
    # determine what pair of inputs produces the output 19690720
    for a in range(100):
        for b in range(100):
            
            cpy = ints.copy()
            cpy[1] = a
            cpy[2] = b

            if IntcodeCompiler(cpy) == 19690720:
                return [a, b]

def main() -> None:
    print('Day 2')
    print('Task 1:', part1())
    print('Task 2:', part2())
    
if __name__ == '__main__':
    main()