import re
lit = [r'\d','one','two','three','four','five','six','seven','eight','nine']

def solve(content, pt2=0, value=0):
    for line in content:
        nums   = re.findall(f"(?=({'|'.join(lit[:len(lit)*pt2+1])}))", line)
        parse  = lambda x: str(lit.index(x)) if(not x.isdigit())*pt2 else x
        value += int(parse(nums[0]) + parse(nums[-1]))
    print(value)

if __name__ == "__main__":
    with open('input/day01.txt') as f:
        content = f.read().splitlines()
        solve(content) # 54561
        solve(content, 1) # 54076