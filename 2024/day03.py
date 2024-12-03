import re

def solve(content, part2=False, value=0, enabled=True):
    for line in content:
        ops = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', line)
        for op in ops:
            if 'do' in op:
                enabled = 't' not in op or not part2
                continue
        
            if enabled:
                x, y = re.findall(r'\d+', op)
                value += int(x) * int(y)
    print(value)

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().splitlines()
        solve(content)              # 180233229
        solve(content, part2=True)  # 95411583
