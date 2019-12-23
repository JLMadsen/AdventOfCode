import re
from collections import defaultdict
# Bad method, but it works...
def getRecipe(filename):
    inputfile = open(filename)
    text = inputfile.read()
    inputfile.close()
    
    lines = text.split('\n')
    recipes = {}
    
    for line in lines:
        list1, list2 = line.split('=>')
        regexp = r'\d+ \w+'
        list1 = re.findall(regexp, list1)
        list2 = re.findall(regexp, list2)
        
        tab = []
        for item in list1:
            num, name = item.split(' ')
            tab.append([int(num), name])
        
        num, name2 = list2[0].split(' ')
        num = int(num)
        
        recipes[name2] = [num]
        for amount, name in tab:
            recipes[name2].append([amount, name])
                
    return recipes
    
def createFuel(recipes):
    queue = ['FUEL']
    counter = defaultdict(lambda: 0)
    oreCount = 0
    
    while 1:
    
        while queue:
            current = queue.pop()
            
            recipe = recipes[current]
            
            amount = recipe[0]
            ingredients = recipe[1:]
            
            multiplier = 1 if not counter[current] else counter[current]//amount
            counter[current] -= amount*multiplier
                    
            for num, name in ingredients:
                if name == 'ORE':
                    oreCount += num*multiplier
                else:
                    queue.append(name)
                    counter[name] += num*multiplier
                    
        for name, amount in counter.items():
            if amount > 0:
                queue.append(name)
                
        if not queue:
            break

    print(counter)
    return oreCount
        
    
def main():
    filename = 'input/day14input.txt'
    recipes = getRecipe(filename)
    oreCount = createFuel(recipes)
    
    print('Part 1', oreCount)
    if oreCount == 210924: print('Wrong answer')
        
if __name__ == '__main__':
    main()