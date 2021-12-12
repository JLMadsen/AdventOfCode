from collections import defaultdict

def create_graph(connections):
    graph = defaultdict(lambda: [])
    for a, b in connections:
        if b != 'start':
            graph[a].append(b)
        if a != 'start':
            graph[b].append(a)
    graph['end'] = []
    return graph

paths = set()

def explore(graph, node, path, small_once, has_two_lower=False):
    if node == 'end':
        paths.add( tuple(path) )
        return

    if node in path and node.islower():
        if small_once:
            return
        else:
            if has_two_lower:
                return
            has_two_lower = True
    
    path.append(node)
    
    for next_node in graph[node]:
        explore(graph, next_node, path[:], small_once, has_two_lower)

def find_path(graph, small_once=True):
    global paths
    paths = set()
    explore(graph, 'start', [], small_once)

    counter = 0
    for path in paths:
        for cave in path:
            if cave.islower():
                counter += 1
                break
    return counter

if __name__ == "__main__":
    with open('input/day12.txt') as f:
        content = [path.split('-') for path in f.read().split('\n')[:-1]]
        graph = create_graph(content)

        print(find_path(graph)) # 3761
        print(find_path(graph, False)) # 99138