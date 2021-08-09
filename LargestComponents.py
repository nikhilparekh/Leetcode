def largestComponents(graph):
    count = res = 0
    visited = set()
    stack = []
    for i in graph:
        if i not in visited:
            stack.append(i)
            while stack:
                for j in graph[stack[0]]:
                    if j not in visited:
                        stack.append(j)
                        visited.add(j)
                        count+=1
                stack.pop(0)
            res = max(count,res)
            count=0
    return res
 

graph = {0:[8,1,5],1:[0],5:[0,8],8:[0,5],2:[3,4],3:[2,4],4:[3,2]}

print(largestComponents(graph))