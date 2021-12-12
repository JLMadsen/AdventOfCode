from collections import defaultdict

def create_graph(connections):
    graph = defaultdict(lambda: [])
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    graph['end'] = []
    return graph

paths = set()

def explore(graph, node, path, small_once):
    if node == 'start' and len(path) != 0:
        return

    if node in path and node.islower():
        if small_once:
            return
        else:
            if any( [ path.count(n) == 2 for n in path if n.islower() ] ):
                return
    
    path.append(node)

    if node == 'end':
        paths.add( tuple(path) )
        return
    
    for next_node in graph[node]:
        explore(graph, next_node, path[:], small_once)

def find_path(graph, small_once=True):

    explore(graph, 'start', [], small_once)

    counter = 0
    for path in paths:
        if any( [ cave.islower() for cave in list(path)[1:-1] ] ):
            counter += 1

    return counter

if __name__ == "__main__":
    with open('input/day12.txt') as f:
        content = [path.split('-') for path in f.read().split('\n')[:-1]]
        graph = create_graph(content)

        print(find_path(graph)) # 3761
        print(find_path(graph, False)) # 99138