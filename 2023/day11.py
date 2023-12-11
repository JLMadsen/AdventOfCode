nth = lambda arr, n: [*zip(*arr)][n-1]

def solve(content, mul, value=0):
    cosmos=[]
    galaxies = set()

    for line in content:
        row = ""
        for i in range(len(line)):
            row += '@'*('#' not in nth(content, i))
            row += line[i]

        if '#' not in line: 
            cosmos.append('@')
        cosmos.append(row)

    y_times = 0
    for y, row in enumerate(cosmos):
        if row == '@': y_times += 1; continue
        x_times = 0
        for x, char in enumerate(row):
            if char == '@': x_times += 1
            if char == '#': galaxies.add((y+((mul-2)*y_times), 
                                          x+((mul-2)*x_times)))

    for ay, ax in galaxies:
        for by, bx in galaxies:
            if (ay, ax) == (by, bx): continue
            value += (abs(by-ay)+abs(bx-ax))/2
    print(int(value))

if __name__ == "__main__":
    with open('input/day11.txt') as f:
        content = f.read().splitlines()
        solve(content, 2)   # 9563821
        solve(content, 1e6) # 827009909817