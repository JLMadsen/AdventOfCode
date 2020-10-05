
def calcPhases(phases, numbers):
    basePattern = [0, 1, 0, -1]
    
    for phase in range(phases):
        
        tab = [0]*len(numbers) # output list
        
        for i in range(len(numbers)):
            
            # get pattern for position
            pattern = []
            for p in basePattern:
                for j in range(i+1):
                    pattern.append(p)
                    
            # make pattern right length for iterating
            pattern = pattern * (len(numbers) // len(pattern) +1)
            pattern = pattern[0:len(numbers)+1]
            pattern.pop(0)
            
            for num, pat in zip(numbers, pattern):
                #print(num, pat)
                tab[i] += (num * pat)
                
            tab[i] = int(str(tab[i])[-1])
            
        numbers = tab.copy()
        
    return numbers

def getAns(tab, jump = 0):
    tab = list(map(str, tab[jump:jump+8]))
    ans = "".join(tab)
    return ans  

def main():
    filename = 'input/day16input.txt'
    phases = 100
    
    #numbers = list(map(int, list(open(filename).read())))
    numbers = [0,3,0,3,6,7,3,2,5,7,7,2,1,2,9,4,4,0,6,3,4,9,1,5,6,5,4,7,4,6,6,4]
    result = calcPhases(phases, numbers.copy())
    
    ans = getAns(result)
    print('Part 1', ans)

    phases = 1000
    result2 = calcPhases(phases, numbers.copy())
    jump = getAns(result2)
    jump = int(jump)//10
    
    ans = getAns(result2, jump)
    print(ans)
    print('Part 2', ans)
    
    
    
if __name__ == '__main__':
    main()