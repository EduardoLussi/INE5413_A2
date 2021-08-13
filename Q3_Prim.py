from math import inf


def Prim(G):
    tamanho = G.qtdVertices()

    A = [None] * tamanho  # Ancestrais dos vértices da árvore
    K = [inf] * tamanho  # Chaves para definir o próximo vértice

    K[0] = 0  # Seleciona um vértice arbitrário para iniciar
              # O valor de i em K[i] pode ser alterado desde que i >= 0 e i < tamanho

    Q = G.vertices  # Cópia dos vértices do grafo
    pesoTotal = 0  # Inicialização do somatório das arestas na árvore

    # Enquanto todos os vértices ainda não forem visitados
    while Q.count(None) < tamanho:
        uIndice = K.index(min(K))
        u = G.vertices[uIndice]
        Q[uIndice] = None  # Marca o vértice como conhecido em Q
        pesoTotal += K[uIndice]
        K[uIndice] = inf  # Marca o vértice como conhecido em K
        for v in G.vizinhos(u):  # Para cada vizinho de u
            vIndice = v.indice - 1
            pesoAtual = G.peso(u, v)
            # Se o vértice ainda não foi adicionado na árvore e o peso atual é menor do que o contido em K
            if not (Q[vIndice] is None) and pesoAtual < K[vIndice]:
                A[vIndice] = u
                K[vIndice] = pesoAtual

    printPrim(pesoTotal, A, tamanho)


# Função auxiliar para imprimir a solução
def printPrim(pesoTotal, A, tamanho):
    print(f"{pesoTotal}")
    msg = ""
    for i in range(0, tamanho):
        if A[i] is not None:
            msg += f"{i + 1}-{A[i].indice}, "
    print(msg[:-2])
