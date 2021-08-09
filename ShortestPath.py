def shortestPath(edges,source,dest):
    def buildPath(edges):
        graph = {}
        for i in edges:
            if i[0] in graph:
                graph[i[0]].append(i[1])
            else:
                graph[i[0]] = [i[1]]
            if i[1] in graph:
                graph[i[1]].append(i[0])
            else:
                graph[i[1]] = [i[0]]
        return graph
    
    graph = buildPath(edges)

    visited = set()
    queue = []
    cur = [source,0]
    queue.append(cur)
    while queue:
        [node, dist] = queue.pop()
        if node==dest:
            return [node,dist]
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.insert(0,[i,dist+1])
    return False





edges = [["w","x"],
        ["x","y"],
        ["z","y"],
        ["z","v"],
        ["w","v"]]

print(shortestPath(edges,"w","z"))