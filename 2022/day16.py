# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
# https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
# https://en.wikipedia.org/wiki/Breadth-first_search

import math
import re
from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

# mapping length to _all_ valves
def breadth_first_search(start):
    queue = [start]
    explored = set(start)
    depth = {start: 0}
    while queue:
        current = queue.pop(0)
        for tunnel in graph[current]:
            if tunnel not in explored:
                explored.add(tunnel)
                depth[tunnel] = depth[current] + 1
                queue.append(tunnel)
    depth.pop(start)
    return depth

def open_valves(current, minutes, output = 0, value = 0 , path = []):
    # print('current', current, 'path', path, output, value)
    max_value = value

    # if more minutes, but no more valves
    if all(valve in path for valve in foo):
        return value + (output * minutes)

    for next_valve in foo:
        if current == next_valve: continue
        if next_valve in path: continue

        path_minutes = minutes - (cost := paths[current][next_valve] + 1)
        next_value = 0
        
        if path_minutes < 0: 
            next_value = value + output * ( cost + path_minutes)
        else:
            path_output = output + flows[next_valve]
            path_value = value + output * (cost)

            next_value = open_valves(next_valve,
                                     path_minutes,
                                     path_output,
                                     path_value,
                                     path + [current])

        max_value = max(next_value, max_value)

    return max_value

def part1(content, minutes = 30, value = 0):
    global graph, flows, paths
    graph = {}                      # A -> [B, C]
    flows = {}                      # A -> 20
    paths = defaultdict(lambda: {}) # A -> {B: 1 min}

    for line in content:
        _, valve, _,_, flow, _,_,_,_, *targets = line.split()
        targets = [*map(lambda s: s[:2], targets)]

        graph[valve] = targets
        flows[valve] = int(flow[5:-1])

    for valve in graph.keys():
        paths[valve] = breadth_first_search(valve)

    # graph = [valve for valve in graph.keys() if flows[valve] > 0]
    global foo
    foo = set()
    for valve in [*graph.keys()]:
        if flows[valve] > 0:
            foo.add(valve)
    # print('non-empty valves', foo)

    current_valve = 'AA'
    value = open_valves(current_valve, minutes)

    print(value)

ex = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

def part2(content):
    pass

if __name__ == "__main__":
    with open('input/day16.txt') as f:
        content = f.read().splitlines()
        content = ex.splitlines()

        part1(content)
        part2(content)