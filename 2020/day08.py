from copy import deepcopy

def run(code):

    hist = set() # all seen pointers
    accu = 0     # accumulator
    curr = 0     # current pointer
    fail = False

    while True:

        # if pointer hits previous or out of bounds
        if curr in hist or 0 > curr > len(code):
            fail = True
            break

        # if pointer reaches end
        if curr == len(code):
            break

        hist.add(curr)

        op, num = code[curr].split(' ')
        num = int(num)

        if op == 'acc':
            accu += num
            curr += 1

        elif op == 'jmp':
            curr += num

        elif op == 'nop':
            curr += 1

    return accu, fail


if __name__ == "__main__":
    with open('2020/input/day08.txt') as f:

        code = f.read().splitlines()

        print( run(code)[0] ) # 1548

        for i in range(len(code)):
            new_code = deepcopy(code)
            op, num = new_code[i].split(' ')

            # changing acc doesnt change anything
            # a jmp 0 results in infinite loop
            # a nop 0 doesnt change anything
            if 'acc' in op or not int(num): continue
            new_code[i] = 'jmp '+ num if 'nop' in op else 'nop '+ num

            val, fail = run(new_code)
            if not fail:
                print(val) # 1375
                break
