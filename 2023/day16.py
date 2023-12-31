up      = (-1,  0)
right   = ( 0,  1)
down    = ( 1,  0)
left    = ( 0, -1)

def energize(content, start, direction, path=set()):
    beams = [(start, direction)]

    while len(beams) > 0:
        new_beams = []
        for (y, x), direction in beams:
            path.add(((y,x),direction))
            dy, dx = (y+direction[0], x+direction[1])

            if dy < 0 or dy >= len(content):    continue
            if dx < 0 or dx >= len(content[0]): continue

            target = (dy, dx)
            char = content[target[0]][target[1]]

            if(char == '.' or 
              (char == '|' and (direction in [up, down])) or 
              (char == '-' and (direction in [right, left]))):
                if (target,direction) not in path:
                    new_beams.append((target, direction))
            elif char in '|-':
                if char == '|':
                    if (target,up) not in path:
                        new_beams.append((target, up))
                    if (target,up) not in down:
                        new_beams.append((target, down))
                else:
                    if (target,left) not in path:
                        new_beams.append((target, left))
                    if (target,right) not in path:
                        new_beams.append((target, right))
            elif char in '\\/':
                if char == '\\':
                    new_dir = (left if direction == up else 
                                       (down if direction == right else 
                                       (up if direction == left else 
                                       (right))))
                    if (target,new_dir) not in path:
                        new_beams.append((target,new_dir))
                else:
                    new_dir = (left if direction == down else 
                                       (down if direction == left else 
                                       (up if direction == right else 
                                       (right))))
                    if (target,new_dir) not in path:
                        new_beams.append((target,new_dir))
        beams = new_beams

    return len({a for a,_ in path}) - 1 

def part1(content): # 8389
    print(energize(content, (0, -1), right))

def part2(content): # 8564
    energies = []
    for i in range(len(content)):
        energies.append( energize(content, (i, -1), right ))
        energies.append( energize(content, (i, len(content[0]) + 1), left ))
    for i in range(len(content)):
        energies.append( energize(content, (-1, i), down ))
        energies.append( energize(content, (len(content), i + 1), up))
    print(max(energies))

if __name__ == "__main__":
    with open('input/day16.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)