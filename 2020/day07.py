import re
from copy import deepcopy
from collections import defaultdict

ruleset = defaultdict(lambda: [])
gold_path = set()

def leads_to_gold(current, path=[]):

    for color in ruleset[current]:
        
        num, *color = color.split(' ')
        color = ' '.join(color)

        if color == 'shiny gold':
            for p in path:
                gold_path.add(p)
        else:
            leads_to_gold(color, deepcopy(path)+[current, color])        

def includes_gold():

    for color in [*ruleset.keys()]:
        leads_to_gold(color)

    print(len(gold_path))

def gold_contains(current):
    count = 0

    for color in ruleset[current]:
        if 'no other' in color:
            return 0

        num, *color = color.split(' ')
        color = ' '.join(color)

        count += (gold_contains(color) * int(num))
        count += int(num)

    return count

if __name__ == "__main__":
    with open('2020/input/day07.txt') as f:

        data = f.read().splitlines()
        for rule in data:      
            left, *right = [* map( lambda x: re.sub(r' bags?', '', x), re.findall(r'\d* ?\w+ \w+ bags?', rule)) ]
            ruleset[left] = right

        includes_gold()                      # 124
        print( gold_contains('shiny gold') ) # 34862