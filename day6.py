# 1735 too low

def createGraph(spaceMap) -> {}:

    graph = {}
    for relation in spaceMap:
        p1, p2 = relation.split(')')
        
        if p1 not in graph.keys():
            # neighbors, direct, indirect
            graph[p1] = [[],0]
        if p2 not in graph.keys():
            graph[p2] = [[],0]

        graph[p1][0].append(p2)

    return graph

def orbitChecksum(graph) -> int:
    checksum = 0

    # start at Center Of Mass
    queue = [graph['COM']]

    while queue:
        current = queue.pop(0)
        
        for neighbor in current[0]:
            next = graph[neighbor]

            # direct and indirect
            indirect = current[1]+1
            next[1] = indirect
            checksum += 1 + indirect

            for n in next[0]:
                queue.append(graph[n])

    for thing in graph.items(): print(thing)
    return checksum

def main() -> None:
    spaceMap = open('input/day6input.txt').read().split()
    spaceTree = createGraph(spaceMap)
    totalOrbit = orbitChecksum(spaceTree)

    print(totalOrbit)

if __name__ == '__main__':
    main()