import queue


def bfs(adj,source):
    visited = set()
    queue = []
    queue.insert(0,source)
    while queue:
        cur = queue.pop()
        print(cur)
        if cur not in visited:
            for i in adj[cur]:
                queue.insert(0,i)
            visited.add(cur)


adj_list = {"a":["c","b"],"b": ["d"],"c": ["e"],"d":["f"],"e":[],"f":[]}
bfs(adj_list,"a")