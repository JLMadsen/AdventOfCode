# https://en.wikipedia.org/wiki/Z3_Theorem_Prover
# https://en.wikipedia.org/wiki/Satisfiability_modulo_theories


def calc(model_number, content):

    register = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    stack = []
    cmds = [line.split() for line in content]
 
    for n in range(14):

        div = int( cmds[ n * 18 + 4  ][-1] )
        chk = int( cmds[ n * 18 + 5  ][-1] )
        add = int( cmds[ n * 18 + 15 ][-1] )

        if div == 1:
            stack.append((n, add))

        elif div == 26:
            m, add = stack.pop()
            model_number[n] = model_number[m] + add + chk

            if model_number[n] > 9:
                model_number[m] -= model_number[n] - 9
                model_number[n] = 9
            
            if model_number[n] < 1:
                model_number[m] += 1 + model_number[n]
                model_number[n] = 1

    return "".join(map(str, model_number))


if __name__ == "__main__":
    with open('input/day24.txt') as f:
        content = f.read().split('\n')[:-1]

        print( calc([9]*14, content) ) # 39924989499969
        print( calc([0]*14, content) ) #