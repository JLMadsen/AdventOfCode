import time
from copy import deepcopy
per_boot = 0.0008392333984375 * 4



def run_once(code):
    acc = 0
    hist = []
    index = 0
    while 1:

        op, num = code[index].split(' ')
        num = int(num)

        if op == 'acc':
            acc += num
            index += 1
            if index in hist:
                break
            hist.append(index)
        elif op == 'jmp':
            index += num
            if index in hist:
                break
            hist.append(index)
        elif op == 'nop':
            index += 1

    print(acc)

def fix_jump(code):
    for i in range(len(code)):
        code_2 = deepcopy(code)
        op, num = code[i].split(' ')
        code_2[i] = 'jmp '+num if op == 'nop' else 'nop '+num

        time_limit = False
        acc = 0
        index = 0
        start = time.time()

        while not time_limit:
            if time.time() - start > per_boot:
                time_limit = True

            if index == len(code_2):
                break

            op, num = code_2[index].split(' ')
            num = int(num)

            if op == 'acc':
                acc += num
                index += 1
            elif op == 'jmp':
                index += num
            elif op == 'nop':
                index += 1

        if not time_limit and index == len(code_2):
            print(acc)
            return

if __name__ == "__main__":
    with open('2020/input/day08.txt') as f:

        data = f.read().splitlines()

        run_once(data) # 1548
        fix_jump(data) # 1375