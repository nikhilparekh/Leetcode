# A program to convert undirectional graph egdes to adj list

def edgesToAdj(edges):
    adj_list = {}
    for i in edges:
        if i[0] in adj_list:
            adj_list[i[0]].append(i[1])
        elif i[0] not in adj_list:
            adj_list[i[0]] = [i[1]]
        if i[1] in adj_list:
            adj_list[i[1]].append(i[0])
        elif i[1] not in adj_list:
            adj_list[i[1]] = [i[0]]
    return adj_list



edges = [["i","j"],["k","i"],["m","k"],["k","l"],["o","n"]]

adj = edgesToAdj(edges)

print(adj)