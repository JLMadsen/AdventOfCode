from copy import deepcopy

class state:
    empty = 'L'
    occupied = '#'
    floor = '.'

def cellular_automata(data, lower, count_floor=True):
    done = False
    while not done:

        done = True # false if seat changes again
        next_state = deepcopy(data)

        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                if cell == state.floor:
                    continue

                count = 0
                for n in [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]:
                    try:
                        i_2, j_2 = n

                        while 1:
                            if (len(data)    > (i+i_2) >= 0 and 
                                len(data[0]) > (j+j_2) >= 0): 

                                looking_at = data[i+i_2][j+j_2]

                                if looking_at == state.floor and not count_floor:
                                    i_2 += n[0]
                                    j_2 += n[1]
                                    continue

                                if looking_at == state.occupied: 
                                    count += 1
                                break
                            else:
                                break
                    except:
                        pass

                if count == 0 and cell == state.empty:
                    next_state[i][j] = state.occupied
                    done = False
                    
                elif count > lower and cell == state.occupied:
                    next_state[i][j] = state.empty
                    done = False

        data = next_state

    print((''.join([''.join(r) for r in data])).count(state.occupied))

if __name__ == "__main__":
    with open('2020/input/day11.txt') as f:

        data = f.read().splitlines()
        data = [[c for c in r] for r in data]

        cellular_automata(data, 3)        # 2093
        cellular_automata(data, 4, False) # 1862
