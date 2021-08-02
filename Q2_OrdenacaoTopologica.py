from grafoDirigido import GrafoDirigido


def imprimirDFS(O):
    output = ''
    for v in O:
        output += f"{v.rotulo} -> "
    output = output[:-4] + "."
    print(output)


def DFS(G):
    C = []
    O = []
    for u in G.vertices:
        if u not in C:
            DFS_Visit_OT(G, u, C, O)
    return O


def DFS_Visit_OT(G, v, C, O):
    C.append(v)
    for u in G.vizinhos(v):
        if u not in C:
            DFS_Visit_OT(G, u, C, O)

    O.insert(0, v)


grafo = GrafoDirigido()
grafo.ler("GrafosTeste/manha.net")
dfs = DFS(grafo)
imprimirDFS(dfs)
