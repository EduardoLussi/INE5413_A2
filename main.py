from grafoDirigido import GrafoDirigido
from grafoNaoDirigido import GrafoNaoDirigido

from Q1_CFC import CFC
from Q2_OrdenacaoTopologica import DFS, imprimirDFS
from Q3_Prim import Prim

op = 1
while op in range(1, 4):
    print(f"\n{'-'*50}")
    print("1- Componentes Fortemente Conexas")
    print("2- Ordenação Topológica")
    print("3- Prim")
    print("4- Sair\n")

    op = int(input("Digite o número da questão: "))

    if op not in range(1, 4):
        break

    name = input("Digite o nome do arquivo: ")   # Inserir arquivo de teste na pasta GrafosTeste

    print()

    if op == 1:
        grafo = GrafoDirigido()

        try: 
            grafo.ler(f"GrafosTeste/{name}")
            CFC(grafo)
        except:
            print("Nome de arquivo inválido")
        
    elif op == 2:
        grafo = GrafoDirigido()

        try: 
            grafo.ler(f"GrafosTeste/{name}")
            dfs = DFS(grafo)    # Cria ordenação topológica
            imprimirDFS(dfs)    # Imprime ordenação topológica conforme padrão definido
        except:
            print("Nome de arquivo inválido")

    elif op == 3:
        grafo = GrafoNaoDirigido()
        
        try: 
            grafo.ler(f"GrafosTeste/{name}")
            Prim(grafo)
        except:
            print("Nome de arquivo inválido")
    else:
        break
