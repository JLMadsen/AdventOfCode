"""
The homework assignment involves adding up a list of snailfish numbers (your puzzle input). 
The snailfish numbers are each listed on a separate line. 
* Add the first snailfish number and the second, 
* then add that result and the third, 
* then add that result and the fourth, 
* and so on until all numbers in the list have been used once.
"""

import re
import math

# If any pair is nested inside four pairs, the leftmost such pair explodes.
def explode(cell):
    print('explode', cell)
    a, b = [*map(int, re.findall(r'\d+', cell))]
    return a, b

# If any regular number is 10 or greater, the leftmost such regular number splits.
def split(num):
    print('split', num)
    a, b = [*map(int, re.findall(r'\d+', cell))]
    res = ""
    if a < b and a > 9:
        div = a / 2
        res = f"[[{math.floor(div)},{math.ceil(div)}], {b}]"
    elif b > 9:
        div = b / 2
        res = f"[{a}, [{math.floor(div)},{math.ceil(div)}]]"

def split2(num):
    print('split', num)
    div = num/2
    return f"[{math.floor(div)},{math.ceil(div)}]"

def add(a, b):
    return f"[{a},{b}]"


def parse(numbers):
    
    value = numbers[0]
    for num in numbers[1:]:
        value = add(num, value)
        done = False
        while not done:
            nest = 0
            new_value = ""
            
            for idx, char in enumerate(value):
                if char == '[': 
                    nest += 1

                    if nest == 5:
                        print(value)
                        print((' '*(idx))+'^ explode')

                        end = idx + value[idx:].index(']') + 1

                        left, right = explode( value[idx:end] )

                        left_string = value[:idx]
                        left_numbers = [*map(int, re.findall(r'\d+', left_string))]
                        
                        if len(left_numbers) > 0:
                            left += left_numbers[-1]
                            i = len(left_string) - 1 - left_string[::-1].index( str(left_numbers[-1]) )
                            left_string = left_string[:i] + str(left) + ',' + left_string[i+(j if (j:=len(str(left))) > 1 else j ):]
                            print( 'left', left_string[:i] +'|'+ str(left) +'|'+ ',' +'|'+ left_string[i+(j if (j:=len(str(left))) > 1 else j-1 ):] )

                        right_string = value[end:]
                        right_numbers = [*map(int, re.findall(r'\d+', right_string))]
                        
                        print('middle', 0)

                        if len(right_numbers) > 0:
                            right += right_numbers[0]
                            i = right_string.index( str(right_numbers[0]) )
                            right_string = right_string[:i] + str(right) + right_string[i+(j-1 if (j:=len(str(right))) > 1 else j ):]
                            print( 'right', right_string[:i] +'|'+ str(right) +'|'+ right_string[i+(j-1 if (j:=len(str(right))) > 1 else j ):])

                        value = f"{left_string}0{right_string}"
                        break

                if char == ']': nest -= 1
            else:
                nn = [*map(int, re.findall(r'\d+', value))]

                if all([n < 10 for n in nn]):
                    done = True
                    break

                for n in nn:
                    if n > 9:
                        i = value.find(str(n))
                        print(value)
                        print((' '*(i))+'^ split')

                        l = len(str(n))
                        res = split2(n)
                        value = value[:i] + res + value[i+l:]
                        break
        print(value)


if __name__ == "__main__":
    with open('input/day18.txt') as f:
        print()

        content = f.read().split('\n')
        #parse(content)
        parse(["[1,1]", "[[[[4,3],4],4],[7,[[8,4],9]]]"])

        print()
"""
[[[[0,7],4],[15,[0,13]]],[1,1]]
[[[[0,7],4],[15,[0,13]]],[1,1]]

[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
[[[[0,7],4],[[7,8],[6,0,0]]],[8,1]]




"""