
def surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])

def ribbon_length(l, w, h):
    return sum([*map(lambda x: x*2, sorted([l,w,h])[:-1])]) + l*w*h

if __name__ == "__main__":
    with open('2015/input/day02.txt') as f:

        data = f.read().splitlines()

        print( sum( [*map( lambda x: surface_area(*[*map(int, x.split('x'))]), data )] ))  # 1588178
        print( sum( [*map( lambda x: ribbon_length(*[*map(int, x.split('x'))]), data )] )) # 3783758