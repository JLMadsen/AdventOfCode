from collections import defaultdict

def valid(pages, before):
    return not any(
        any(
            preceding in pages[:i]
            for preceding in before[page]
        )
        for i, page in enumerate(pages)
    )

def solve(content, p1=0, p2=0):
    before = defaultdict(list)

    for line in content:
        if '|' in line:
            a, b = line.split('|')
            before[a].append(b)

        if ',' in line:
            pages = line.split(',')
            if valid(pages, before):
                p1 += int(pages[ len(pages) // 2 ])
                continue

            while not valid(pages, before):
                for i, page in enumerate(pages):
                    for preceding in before[page]:
                        if preceding in pages[:i]:

                            index = pages.index(preceding)
                            pages.remove(page)
                            pages[index:index] = [page]

                            break
                    else:
                        continue
                    break
            
            p2 += int(pages[ len(pages) // 2 ])

    print(p1) # 6051
    print(p2) # 5093

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().splitlines()
        solve(content)