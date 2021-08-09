from math import inf
from grafoNaoDirigido import GrafoNaoDirigido


def Prim(G):
    tamanho = G.qtdVertices()

    A = [None] * tamanho
    K = [inf] * tamanho

    K[3] = 0

    Q = G.vertices
    pesoTotal = 0

    while Q.count(None) < tamanho:
        uIndice = K.index(min(K))
        u = G.vertices[uIndice]
        Q[uIndice] = None
        pesoTotal += K[uIndice]
        K[uIndice] = inf
        for v in G.vizinhos(u):
            vIndice = v.indice-1
            pesoAtual = G.peso(u, v)
            if not(Q[vIndice] is None) and pesoAtual < K[vIndice]:
                A[vIndice] = u
                K[vIndice] = pesoAtual

    printPrim(pesoTotal, A, tamanho)


def printPrim(pesoTotal, A, tamanho):
    print(f"{pesoTotal}")
    msg = ""
    for i in range(0, tamanho):
        if A[i] is not None:
            msg += f"{i+1}-{A[i].indice}, "
    print(msg[:-2])


grafo = GrafoNaoDirigido()
grafo.ler("GrafosTeste/teste_de_mesa_Prim.net")  # Diretório do arquivo
Prim(grafo)