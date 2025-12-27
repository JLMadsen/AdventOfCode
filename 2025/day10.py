from re import findall
from copy import deepcopy

def format(arr):
    return ''.join(arr)

def part1(content):
    value = 0

    for line in content:
        config, *buttons, _ = line.split()
        config = config[1:-1]
        queue = [('.'*len(config), 0)]
        visited = set()

        done = False
        while not done:
            queue.sort(key=lambda e: e[1])
            state, presses = queue.pop(0)

            for button in buttons:
                new_state = [*state]
                button = findall(r'\d+', button)
                
                for index in map(int, button):
                    new_state[index] = '#' if new_state[index] == '.' else '.'

                if format(new_state) == config:
                    done = True
                    value += presses + 1
                    break
                
                new_new_state = format(new_state)
                if new_new_state not in visited:
                    visited.add(new_new_state)
                    queue.append((new_new_state, presses + 1))

    print(value)

test = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

def part2(content):

    value = 0

    for line in content:
        config, *buttons, joltage = line.split()
        config = config[1:-1]
        joltages = [*map(int, findall(r'\d+', joltage))]

        # print(config, buttons, joltage)

        queue = [('.'*len(config), 0, [], [0 for _ in range(len(joltages))])]
        visited = set()

        done = False
        while not done:
            queue.sort(key=lambda e: e[1])
            state, presses, path, joltage = queue.pop(0)
            # print(queue)
            # print()
            # print('queue', len(queue), 'visited', len(visited), 'origin', state, presses, joltage)

            # if presses > 5:
            #     print('ERROR')
            #     break

            solution = [0,1,1,1,3,3,3,4,5,5]

            if path == solution:
                print('RIIIIIIIKTIIIIIIIIG')
                print('queue', len(queue), 'visited', len(visited), 'origin', state, presses, joltage)
                print('correctish', format(new_state), new_joltage, path)
                exit()
            
            if presses > 10:
                print('passed')
                exit()

            for button in buttons:
                new_state = deepcopy([*state])
                new_joltage = deepcopy(joltage)
                
                # print(format(new_state), button, presses)
                for index in map(int, findall(r'\d+', button)):
                    new_state[index] = '#' if new_state[index] == '.' else '.'
                    new_joltage[index] += 1
                # print(format(new_state),'\t', config)
                # print()

                if any(a > b for a, b in zip(new_joltage, joltages)):
                    # print(new_joltage, joltages)
                    continue
                
                if format(new_state) == config:
                    print('queue', len(queue), 'visited', len(visited), 'origin', state, presses, joltage)
                    print('correctish', format(new_state), new_joltage, path)

                if format(new_state) == config and new_joltage == joltages:
                    done = True
                    value += presses + 1
                    # print(format(new_state), config, presses, path)
                    break
                
                new_new_state = format(new_state)
                if (new_new_state + str(joltage) + str(presses)) not in visited:
                    visited.add(new_new_state + str(joltage) + str(presses))
                    queue.append((new_new_state, presses + 1, [*path, buttons.index(button)], new_joltage))

    print(value)

if __name__ == '__main__':
    with open("./input/day10.txt") as f:
        # content = f.read().splitlines()
        content = test.splitlines()
        # part1(content) # 438
        part2(content) # 