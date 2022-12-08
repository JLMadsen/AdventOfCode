def part1(grid, value = 0):
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):

            for mod in [(0,1),(0,-1),(-1,0),(1,0)]:
                dx, dy = x, y
                done = False
                while True:

                    dx, dy = dx+mod[0], dy+mod[1]
                    if ((dy == len(grid) or dy == -1) or 
                        (dx == len(row) or dx == -1)):
                        value += 1
                        done = True
                        break

                    if grid[dy][dx] >= tree: break
                if done:break

    print(value) # 1698

def part2(grid, value = 0):
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            scenic_score = 1

            for mod in [(0,1),(0,-1),(-1,0),(1,0)]:
                dx, dy = x+mod[0], y+mod[1]
                directional_score = 0

                while 0 <= dy < len(grid) and 0 <= dx < len(row):
                    
                    directional_score += 1
                    if grid[dy][dx] >= tree: break
                    dx, dy = dx+mod[0], dy+mod[1]

                scenic_score *= directional_score
            
            if scenic_score > value:
                value = scenic_score

    print(value) # 672280

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().splitlines()
        part1([[int(c) for c in line] for line in content])
        part2([[int(c) for c in line] for line in content])