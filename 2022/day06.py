def solve(content, length, buffer = ''):
    print([idx + length for idx, string in enumerate(
          [*zip([zip(content[n:n+length]) for n in range(len(content)-length+1)])])
          if len(set([''.join(''.join(map(lambda x: x[0],a))) for a in string][0])) ==  length
        ][0])

if __name__ == "__main__":
    with open('input/day06.txt') as f:
        content = f.read().splitlines()[0]
        solve(content, 4) # 1598
        solve(content, 14) # 2414
