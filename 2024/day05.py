
from collections import defaultdict

def check(pages, before):
    viewed_pages = []
    for page in pages:
        if any(b in viewed_pages for b in before[page]):
            return False
        viewed_pages.append(page)
    return True

def solve(content, p1=0, p2=0):
    before = defaultdict(list)
    for line in content:
        if '|' in line:
            a, b = line.split('|')
            before[a].append(b)

        if ',' in line:
            pages = line.split(',')
            if check(pages, before):
                p1 += int(pages[ len(pages) // 2 ])
                continue
            
            corrected = pages
            while not check(corrected, before):
                viewed_pages = []
                edited = False
                
                for page in corrected:
                    for preceding in before[page]:
                        if preceding in viewed_pages:

                            index = corrected.index(preceding)
                            corrected.remove(page)
                            corrected[index:index] = [page]

                            edited = True
                            break
                    if edited:
                        break

                    viewed_pages.append(page)
            
            p2 += int(corrected[ len(corrected) // 2 ])

    print(p1) # 6051
    print(p2) # 5093

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        content = f.read().splitlines()
        solve(content)
