def hasPath(adj_list,source,dest):
    stack = []
    stack.append(source)
    while stack:
        x = stack.pop(0)
        if dest in adj_list[x]:
            return True
        else:
            for i in adj_list[x]:
                stack.append(i)
    return False






adj_list = {"a":["b","c"],"b": ["d"],"c": ["e"],"d":[],"e":["b"],"f":["d"]}

print(hasPath(adj_list,"c","d"))

