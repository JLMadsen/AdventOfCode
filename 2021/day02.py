import math

def get_pos(inst, x=0, y=0):
    return math.prod([(x:=x+((int(b[1]) * (1 if b[0] in 'down' else -1)) if b[0] in ['down', 'up'] else 0), y:=y+(int(b[1]) if b[0] in ['forward'] else 0)) for line in inst if (b:=line.split())][-1])

def get_pos2(inst, x=0, y=0, d=0):
    return math.prod([(d:=d+((int(b[1]) * (1 if b[0] in 'down' else -1)) if b[0] in ['down', 'up'] else 0), y:=y+(int(b[1]) if b[0] in ['forward'] else 0), x:=x+(d*int(b[1]) if b[0] in ['forward'] else 0)) for line in inst if (b:=line.split())][-1][1:])

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().split('\n')[:-1]

        print(get_pos(content)) # 1451208
        print(get_pos2(content)) # 1620141160
