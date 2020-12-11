from itertools import permutations


def crack_cipher(data):

    for i in range(len(data)):
        if i < 25: continue

        valid = True
        for j in range(25):
            if not valid: break
            for l in range(j+1, i):
                if data[i-25+j]+data[i-25+l] == data[i]:
                    valid = False
                    break
        else:
            print(data[i])
            return

def continous_numbers_equals_to(data, num):

    for i in range(len(data)):
        counter = data[i]
        numbers = [counter]
        current = i

        while counter < num:
            current += 1
            counter += data[current]
            numbers.append(data[current])

        if counter == num:
            print(min(numbers)+max(numbers))
            return
    
if __name__ == "__main__":
    with open('2020/input/day09.txt') as f:

        data = [*map(int, f.read().splitlines())]

        crack_cipher(data)                          # 22406676
        continous_numbers_equals_to(data, 22406676) # 2942387