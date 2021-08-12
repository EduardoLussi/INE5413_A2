from grafoDirigido import GrafoDirigido
from grafoNaoDirigido import GrafoNaoDirigido

from Q1_CFC import CFC
from Q2_OrdenacaoTopologica import DFS, imprimirDFS

op = 1
while op in range(1, 4):
    name = input("Digite o nome do arquivo: ")   # Inserir arquivo de teste na pasta GrafosTeste

    op = int(input("Digite o número da questão: "))

    if op == 1:
        grafo = GrafoDirigido()

        try: 
            grafo.ler(f"GrafosTeste/{name}")
        except err:
            print("Nome de arquivo inválido")
        
        CFC(grafo)
    elif op == 2:
        grafo = GrafoDirigido()

        try: 
            grafo.ler(f"GrafosTeste/{name}")
        except:
            print("Nome de arquivo inválido")

        dfs = DFS(grafo)    # Cria ordenação topológica
        imprimirDFS(dfs)    # Imprime ordenação topológica conforme padrão definido

    print()
