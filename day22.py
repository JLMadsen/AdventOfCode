import re
DECK_SIZE = 10006

def part1(deck) -> int:
    filename = 'input/day22input.txt'
    instructions = open(filename).read().split('\n')
        
    for instruction in instructions:
        
        op = re.findall(r'[^\d-]+', instruction)
        op = op[0].strip()
        
        if op == 'deal into new stack':
            deck = deck[::-1]
            
        elif op == 'cut':
            num = re.findall(r'\d+', instruction)
            num = int(num[0])
            if num > 0:
                cut = deck[0:num]
                deck = deck[num:] + cut
            else:
                num = abs(num)
                cut = deck[num:]
                deck = cut + deck[0:num]
                
        elif op == 'deal with increment':
            num = re.findall(r'\d+', instruction)
            num = int(num[0])
            newdeck = [0]*DECK_SIZE
            for i in range(len(deck)):
                newdeck[(i*num)%DECK_SIZE] = deck[i]
            
            deck = newdeck
            
    print('Part 1', deck[2019])
    
def main() -> None:
    
    deck = list(range(DECK_SIZE))
    part1(deck.copy())

if __name__ == '__main__':
    main()