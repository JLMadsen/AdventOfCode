from collections import deque
# https://docs.python.org/3/library/collections.html#collections.deque

def solve(content, pt2 = False):
    content = deque([*map(lambda n: int(n) * (811589153 if pt2 else 1), content)])
    indexes = deque(range(0, (length := len(content))))

    for _ in range(10 if pt2 else 1):
        for idx in range(length):
            position = indexes.index(idx)
            
            content.rotate(position * -1)
            current_value = content.popleft()
            content.rotate(current_value * -1)
            content.appendleft(current_value)

            indexes.rotate(position * -1)
            current_index = indexes.popleft()
            indexes.rotate(current_value * -1)
            indexes.appendleft(current_index)

    zero = content.index(0)
    a, b, c = (content[(zero + 1000) % (len(content))],
               content[(zero + 2000) % (len(content))],
               content[(zero + 3000) % (len(content))])

    print(sum([a,b,c]))

if __name__ == "__main__":
    with open('input/day20.txt') as f:
        content = f.read().splitlines()
        solve(content) # 11123
        solve(content, True) # 4248669215955