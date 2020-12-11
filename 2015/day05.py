
vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']

def validate_string_1(data):
    count = 0
    
    for string in data:
        v_count = 0 # vowels

        for char in vowels:
            v_count += string.count(char)
        
        if v_count < 3:
            continue

        for i,c in enumerate(string[:-1]):
            if string[i+1] == c:
                break
        else:
            continue
        
        if any( pair in string for pair in forbidden ):
            continue

        count += 1
    print(count)

def validate_string_2(data):
    count = 0

    for string in data:

        for i,c in enumerate(string[:-2]):
            if string[i+2] == c:
                break
        else:
            continue

        pair_repeats = False
        for i,c in enumerate(string[:-1]):
            pair = c+string[i+1]
            next_pair = string[i+2:].find(pair)
            if next_pair != -1:
                pair_repeats = True
                #print(string)
                #print(' '*i +'^' + ' '*(next_pair+1)+'^')
                break

        if pair_repeats:
            count += 1
    print(count)
        
    

if __name__ == "__main__":
    with open('2015/input/day05.txt') as f:

        data = f.read().splitlines()

        validate_string_1(data) # 236
        validate_string_2(data) # 51
