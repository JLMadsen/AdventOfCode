# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
# https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
# https://en.wikipedia.org/wiki/Breadth-first_search

import math
import re
from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

def breadth_first_search(start, goal):
    queue = [start]
    explored = set(start)
    depth = 0
    while queue:
        current = queue.pop(0)
        print(current)
        if current == goal:
            return depth
        for tunnel in graph[current]:
            queue.append(tunnel)

def part1(content, minutes = 30, value = 0):
    global graph, flows, paths
    graph = {}                          # A -> [B, C]
    flows = {}                          # A -> 20
    paths = defaultdict(lambda: {})     # A -> {B: 1 min}

    opened = set()

    for line in content:
        _, valve, _,_, flow, _,_,_,_, *targets = line.split()
        targets = [*map(lambda s: s[:2], targets)]

        graph[valve] = targets
        flows[valve] = int(flow[5:-1])

    for valve1, _ in graph.items():
        for valve2 in graph.keys():
            if valve1 == valve2: continue
            paths[valve1][valve2] = breadth_first_search(valve1, valve2)

    current_valve = 'AA'







    print(paths)

def part2(content):
    pass

if __name__ == "__main__":
    with open('input/day16.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)
