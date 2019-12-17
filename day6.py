# https://adventofcode.com/2019/day/6

def createGraph(spaceMap) -> {}:

    graph = {}
    for relation in spaceMap:
        p1, p2 = relation.split(')')
        
        if p1 not in graph.keys():
            # neighbors, indirect, predecessor
            graph[p1] = [[],0,'']
        if p2 not in graph.keys():
            graph[p2] = [[],0,'']

        graph[p1][0].append(p2)
        graph[p2][2] = p1

    return graph

def orbitChecksum(graph) -> int:
    checksum = 0

    # start at Center Of Mass
    queue = ['COM']
    visited = []

    while queue:
        planetName = queue.pop(0)
        current = graph[planetName]

        for neighbor in current[0]:

            graph[neighbor][1] = current[1]+1
            checksum += current[1]+1
            queue.append(neighbor)

    #for n in graph.items(): print(n)
    return checksum

def makeGraphUndirected(graph_) -> {}:
    graph = {}
    for node in graph_.keys():
        graph[node] = []
        oldNode = graph_[node]
        for neighbor in oldNode[0]: graph[node].append(neighbor)
        graph[node].append(oldNode[2])
    
    return graph

def pathToSanta(graph_, visited = [], predecessors = {}) -> int:

    graph = makeGraphUndirected(graph_.copy())
    
    queue = ['YOU']
    goal = 'SAN'

    visited.append('YOU')
    predecessors['YOU'] = -1

    while queue:
        planetName = queue.pop(0)
        if planetName == '': continue
        if planetName == goal: break # optimization

        current = graph[planetName]
        visited.append(planetName)

        for neighbor in current:

            if neighbor not in visited:
                predecessors[neighbor] = planetName
                queue.append(neighbor)

    path = ['SAN']
    current = predecessors[goal]
    while current != -1:
        path.append(current)
        current = predecessors[current]

    for i in range(len(path)):
        for j in range(i+1, len(path)):
            if path[i] == path[j]:
                print('e', path[i], i)

    print(path)
    return len(path)

def main() -> None:
    spaceMap = open('input/day6input.txt').read().split()
    spaceTree = createGraph(spaceMap)
    totalOrbit = orbitChecksum(spaceTree)    

    print('Part 1 =', totalOrbit)

    pathLength = pathToSanta(spaceTree)
    print('Part 2 =', pathLength) # not 376

if __name__ == '__main__':
    main()