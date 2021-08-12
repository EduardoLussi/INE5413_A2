from math import inf
from grafoDirigido import GrafoDirigido


def CFC(G):
    C, T, A, F = DFS(G)  # DFS com o grafo normal

    # Criação do Grafo transposto
    Gt = GrafoDirigido()
    Gt.definirVertices(G.vertices)
    for a in G.arcos:
        Gt.inserirArco(a.destino, a.origem, a.peso)

    # DFS adaptada para navegar pela F em ordem decrescente
    Ct, Tt, At, Ft = DFS_adaptado(Gt, F)

    printCFC(At)


def DFS(G):
    tamanho = G.qtdVertices()

    # Inicialização dos vetores
    C = [False] * tamanho
    T = [inf] * tamanho
    F = [inf] * tamanho
    A = [None] * tamanho
    tempo = [0]

    for u in G.vertices:  # Para cada vizinho de u
        if not(C[u.indice-1]):  # Se u não for conhecido
            DFS_Visit(G, u, C, T, A, F, tempo)
    return C, T, A, F


def DFS_adaptado(G, Fd):
    tamanho = G.qtdVertices()

    # Inicialização dos vetores
    C = [False] * tamanho
    T = [inf] * tamanho
    F = [inf] * tamanho
    A = [None] * tamanho
    tempo = [0]

    for i in range(0, tamanho):
        # Parâmetros para manter a ordem decrescente de F
        maior = max(Fd)
        indice = Fd.index(maior)
        Fd[indice] = -1
        if not(C[indice]):  # Se o vértice da vez não for conhecido
            DFS_Visit(G, G.obterVertice(indice+1), C, T, A, F, tempo)
    return C, T, A, F


def DFS_Visit(G, v, C, T, A, F, tempo):
    C[v.indice-1] = True
    tempo[0] += 1
    T[v.indice-1] = tempo
    for u in G.vizinhos(v):  # Para cada vizinho de u
        if not(C[u.indice-1]):  # Se u não for conhecido
            A[u.indice-1] = v
            DFS_Visit(G, u, C, T, A, F, tempo)

    tempo[0] += 1
    F[v.indice-1] = tempo[0]


# Funções auxiliares para imprimir os CFCs
def printCFC(A):
    tamanho = len(A)
    for i in range(0, tamanho):
        if A[i] is None:
            R = []
            printCFCHelper(tamanho, i, A, R)
            print(str(sorted(R))[1:-1].replace(" ", ""))


def printCFCHelper(tamanho, i, A, R):
    indice = i + 1
    R.append(indice)
    for j in range(0, tamanho):
        if A[j] is not None and A[j].indice == indice:
            printCFCHelper(tamanho, j, A, R)
