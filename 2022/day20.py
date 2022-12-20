from collections import deque

def solve(content, pt2 = False, current_value = 0):
    content = deque([*map(lambda n: int(n) * (811589153 if pt2 else 1), content)])
    indexes = deque(range(0, (length := len(content))))

    for _ in range(10 if pt2 else 1):
        for idx in range(length):
            position = indexes.index(idx)
            for deq in [content, indexes]:
                deq.rotate(position * -1)
                local_value = deq.popleft()
                if deq == content: current_value = local_value
                deq.rotate(current_value * -1)
                deq.appendleft(local_value)

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