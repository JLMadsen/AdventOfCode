from copy import deepcopy
import random

class state:
    empty = 'L'
    occupied = '#'
    floor = '.'

def direction(i, j, data):
    pos = []
    for d in [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[1,-1],[-1,+1]]:
        n = deepcopy(d)
        try:
            while data[i+n[0]][j+n[1]] == state.floor:
                n[0] += n[0]
                n[1] += n[1]
        except:
            pass
        pos.append([i+n[0],j+n[1]])

    return pos

def cellular_automata(data, criteria, lower):

    done = False
    it, tr = 0, 1

    while not done:

        done = True # false if seat changes again
        next_state = deepcopy(data)

        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                if cell == state.floor:
                    continue

                count = 0

                for n in criteria(i, j, data):
                    try:
                        i_2, j_2 = n
                        #print(i,j,i_2, j_2)

                        if (len(data)    > i_2 >= 0 and 
                            len(data[0]) > j_2 >= 0): 

                            tmp = data[i_2][j_2]
                            if tmp == state.occupied: 
                                count += 1
                    except:
                        pass

                if count == 0 and cell == state.empty:
                    next_state[i][j] = state.occupied
                    done = False
                
                elif count > lower and cell == state.occupied:
                    next_state[i][j] = state.empty
                    done = False

        data = next_state

        it+=1
        if it == tr:
            for row in data:
                print(''.join(row))
            exit()

    res = (''.join([''.join(r) for r in data])).count(state.occupied)

    for row in data:
        continue
        print(''.join(row))

    print(res)

    if res >= 1890:
        print('too high')

if __name__ == "__main__":
    with open('2020/input/day11.txt') as f:

        data = f.read().splitlines()
        data = [[c for c in r] for r in data]

        adjacent  = lambda x, y, *_: [(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x-1,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1)]

        #cellular_automata(data, adjacent, 3)  # 2093
        cellular_automata(data, direction, 4) #
