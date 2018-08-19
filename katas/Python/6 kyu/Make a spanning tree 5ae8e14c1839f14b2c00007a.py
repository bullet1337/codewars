# https://www.codewars.com/kata/5ae8e14c1839f14b2c00007a
def make_spanning_tree(edges, t):
    edge_dict = {}
    vert_dict = {}
    for edge, weight in edges:
        if edge[0] != edge[1]:
            edge_dict[edge] = (min if t == 'min' else max)(edge_dict.get(edge, weight), weight)
            for v in edge:
                if v not in vert_dict:
                    vert_dict[v] = len(vert_dict)
    
    edges = []
    vert_dict_inv = {v: {k} for k, v in vert_dict.items()}
    for edge, weight in sorted(edge_dict.items(), key=lambda x: x[1], reverse=t == 'max'):
        s0, s1 = vert_dict[edge[0]], vert_dict[edge[1]]
        if s0 != s1:
            for v in vert_dict_inv[s1]:
                vert_dict[v] = s0
            vert_dict_inv[s0].update(vert_dict_inv[s1])
            vert_dict_inv.pop(s1)
            edges.append((edge, weight))
    
    return edges