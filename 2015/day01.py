content = open('2015/input/day01.txt').read()

print( content.count('(') - content.count(')') ) # 73

floor = 0
print([i+1 for i,c in enumerate(content) if (floor:=floor-1 if ')' in c else floor+1)<0][0]) # 1795
