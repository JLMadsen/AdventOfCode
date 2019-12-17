import types

"""
Notes:

0, position mode
1, immediate mode

Parameters that an instruction writes to will never be in immediate mode.

"""

class Compiler:

    def __init__(self):
        self.opcodes = [1,2,3,4,5,6,7,8,9]
        self.input = []

    def reset(self):
        self.index = 0

    def load(self, program, size = 1000):
        self.program = program + [0 for i in range(size)]
        self.index = 0

    def getProgram(self, filename = ''):
        if filename != '':
            return list(map(int, open(filename).read().split(',')))
        return self.program

    def loadFilename(self, filename):
        self.program = list(map(int, open(filename).read().split(',')))
        self.index = 0

    def addInput(self, n):
        if isinstance(n, list):
            self.input += n
        else:
            self.input.append(n)

    def run(self, input = [], debug = False):
        output = []
        inputCounter = 0
        relativeBase = 0

        if debug: print('a b c |de | 1 2 3')

        while True:

            # get current opcode and params
            current = self.program[self.index]

            a = current // 10000 % 10
            b = current // 1000 % 10
            c = current // 100 % 10
            de = current % 100

            # exit condition
            if de not in self.opcodes:
                if de != 99: exit('Non 99 exit condition '+ str(de))
                self.reset()
                return [self.program, output]

            addr1 = self.program[self.index + 1]
            addr2 = self.program[self.index + 2]
            addr3 = self.program[self.index + 3]

            try:
                value1 = addr1 if c == 1 else self.program[addr1]
                value2 = addr2 if b == 1 else self.program[addr2]
                value3 = addr3 if a == 1 else self.program[addr3]

                if c == 2: 
                    relativeBase += addr1
                    value1 = self.program[relativeBase]
                    addr1 = value1
                if b == 2:
                    relativeBase += addr2
                    value2 = self.program[relativeBase]
                    addr2 = value2
                if a == 2:
                    relativeBase += addr3
                    value3 = self.program[relativeBase]
                    addr3 = value3
            except:
                pass

            if debug: print(a, b, c, '|', de, '|', addr1, addr2, addr3)

            # run opcode
            if de == 1:
                if addr3 < 0: exit('Negative address')
                self.program[addr3] = value1 + value2
                self.index += 4

            elif de == 2:
                if addr3 < 0: exit('Negative address')
                self.program[addr3] = value1 * value2
                self.index += 4

            elif de == 3:
                if addr1 < 0: exit('Negative address')                
                self.program[addr1] = input[inputCounter]
                inputCounter += 1
                self.index += 2

            elif de == 4:
                output.append(value1)
                self.index += 2

            elif de == 5:
                if value1 != 0:
                    self.index = value2
                else:
                    self.index += 3

            elif de == 6:
                if value1 == 0:
                    self.index = value2
                else:
                    self.index += 3
            
            elif de == 7:
                if addr3 < 0: exit('Negative address')
                self.program[addr3] = 1 if value1 < value2 else 0
                self.index += 4
            
            elif de == 8:
                if addr3 < 0: exit('Negative address')
                self.program[addr3] = 1 if value1 == value2 else 0
                self.index += 4

            elif de == 9:
                relativeBase += value1
                self.index += 2

# run test
import os
if __name__ == '__main__':
    os.system('python IntcodeCompilerTest.py')