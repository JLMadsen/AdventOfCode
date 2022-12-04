def solve(content, includes = 0, value = 0):
    for line in content:
        ax, ay, bx, by = map(int, line.replace('-', ',').split(','))
        value += (1 if (ax>=bx and ay<=by) or 
                       (bx>=ax and by<=ay) or 
                       (bx>=ay and by<=ax and includes) or
                       (by>=ax and bx<=ay and includes) else 0)
    print(value)

if __name__ == "__main__":
    with open('input/day04.txt') as f:
        content = f.read().splitlines()
        solve(content) # 431
        solve(content, 1) # 823