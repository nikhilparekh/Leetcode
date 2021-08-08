def connectedComponents(graph):
    stack = []
    visited = set()
    count = 0
    for i in graph:
        if i not in visited:
            stack.append(i)
            while stack:
                for j in graph[stack[0]]:
                    if j not in visited:
                        stack.append(j)
                        visited.add(j)
                stack.pop(0)
            count+=1
    return count


graph = {
    3:[], 4:[6],6:[4,5,7,8],8:[6],7:[6],5:[6],1:[2],2:[1]
}

print(connectedComponents(graph))