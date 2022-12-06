def solve(content, length, value = 0, buffer = ''):
    for idx, char in enumerate(content[0]):
        buffer += char
        if len(buffer) == (length + 1): buffer = buffer[1:]
        if len(set(buffer)) == length:
            value = idx+1
            break

    print(value)

if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().splitlines()
        solve(content, 4) # 1598
        solve(content, 14) # 2414
