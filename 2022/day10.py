p = [20, 60, 100, 140, 180, 220]

def solve(content, value = 0, register = 1, 
          cycle = 0, monitor = ""):

    for line in content:
        mod = lambda x: (x+1)//40
        pxl = lambda: abs(cycle -1- (register + 40 * mod(cycle))) < 2

        def cycle_once():
            nonlocal cycle, value, monitor
            cycle += 1
            if cycle in p: value += cycle * register
            monitor += '#' if pxl() else ' '

        cycle_once()
        if 'addx' in line:
            cycle_once()            
            register += int(line.split()[1])

    print(value) # 14720
    print('', *[''.join([ c + (' ' if (i+1)%5==0 else '') 
        for i,c in enumerate(monitor[i*40:i*40+40])]) + '\n' 
            for i in range(6)]) # FZBPBFZF

if __name__ == '__main__':
    with open('./input/day10.txt') as f:
        content = f.read().splitlines()
        solve(content)