# 1735 too low

def createGraph(spaceMap) -> {}:

    graph = {}
    for relation in spaceMap:
        p1, p2 = relation.split(')')
        
        if p1 not in graph.keys():
            # neighbors, indirect
            graph[p1] = [[],0]
        if p2 not in graph.keys():
            graph[p2] = [[],0]

        graph[p1][0].append(p2)

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

def main() -> None:
    spaceMap = open('input/day6input.txt').read().split()
    spaceTree = createGraph(spaceMap)
    totalOrbit = orbitChecksum(spaceTree)

    print(totalOrbit)

if __name__ == '__main__':
    main()