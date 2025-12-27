from re import findall
from functools import cache

def part1(content):
    value = 0
    graph = {}
    origin = "you"

    for line in content:
        node, *edges = findall(r'\w+', line)
        graph[node] = edges

    queue = [origin]

    while len(queue) > 0:
        node = queue.pop(0)

        for edge in graph[node]:
            if edge == 'out':
                value += 1
            else:
                queue.append(edge)

    print(value)    

def part2(content):
    graph = {}
    origin = "svr"

    for line in content:
        node, *edges = findall(r'\w+', line)
        graph[node] = edges

    @cache
    def depth_first_search(node, fft, dac):
        if node == "out":
            return fft and dac
        
        edges = graph[node]
        fft = node == 'fft' or fft
        dac = node == 'dac' or dac

        paths = 0
        for edge in edges:
            paths += depth_first_search(edge, fft, dac)
        
        return paths

    print(depth_first_search(origin, 0, 0))

if __name__ == '__main__':
    with open("./input/day11.txt") as f:
        content = f.read().splitlines()
        part1(content) # 772
        part2(content) # 423227545768872