def imprimirDFS(O): # O é a ordenação topológica
    output = ''
    for v in O:
        output += f"{v.rotulo} -> "
    output = output[:-4] + "."
    print(output)


def DFS(G):
    C = []  # Lista de vértices visitados
    O = []  # Ordenação topológica
    for u in G.vertices:
        if u not in C:  # Se u não estiver na lista
            DFS_Visit_OT(G, u, C, O)
    return O


def DFS_Visit_OT(G, v, C, O):
    C.append(v) # Adiciona v na lista de visitados
    for u in G.vizinhos(v): # Para cada vizinho de u
        if u not in C:  # Se u não estiver na lista
            DFS_Visit_OT(G, u, C, O)

    O.insert(0, v)
