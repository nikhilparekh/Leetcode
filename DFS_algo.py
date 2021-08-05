def dfs(adj,source):
    stack = []
    visited = set()
    stack.append(source)
    while stack:
        x = stack.pop()
        if x not in visited:
            for i in adj[x]:
                stack.append(i)
            print(x)
            visited.add(x)


adj_list = {"a":["c","b"],"b": ["d"],"c": ["e"],"d":["f"],"e":[],"f":[]}

dfs(adj_list,"a")



