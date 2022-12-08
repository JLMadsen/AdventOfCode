def solve(content, visible = 0, scenic = 0):
    grid = [[int(c) for c in line] for line in content]

    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            
            scenic_score = 1
            is_visible = False

            for mod in [(0,1),(0,-1),(-1,0),(1,0)]:
                dx, dy = x+mod[0], y+mod[1]
                directional_score = 0
                
                while 0 <= dy < len(grid) and 0 <= dx < len(row):

                    directional_score += 1
                    if grid[dy][dx] >= tree: break
                    dx, dy = dx+mod[0], dy+mod[1]

                if ((dy == len(grid) or dy == -1) or 
                    (dx == len(row) or dx == -1)):
                    visible += 1 if not is_visible else 0
                    is_visible = True
                
                scenic_score *= directional_score

            if scenic_score > scenic:
                scenic = scenic_score

    print(visible) # 1698
    print(scenic) # 672280

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().splitlines()
        solve(content)