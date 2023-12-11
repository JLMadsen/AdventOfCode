nth = lambda arr, n: [*zip(*arr)][n-1]

def solve(content, distance, value=0):
    y_times = 0
    galaxies = set()
    for y, row in enumerate(content):
        y_times += '#' not in row
        x_times = 0
        for x, char in enumerate(row):
            x_times += '#' not in nth(content, x)
            if char == '#':
                galaxies.add((y+((distance-1)*y_times), 
                              x+((distance-1)*x_times)))
            
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