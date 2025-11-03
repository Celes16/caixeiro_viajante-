
import time
from le_matriz import ler_matriz_adjacencia

def algoritmo_vizinho_mais_proximo(matriz_adjacencia):
    
    num_cidades = len(matriz_adjacencia)
    cidade_atual = 0
    caminho = [cidade_atual]
    visitadas = [False] * num_cidades
    visitadas[cidade_atual] = True
    custo_total = 0

    while len(caminho) < num_cidades:
        vizinho_mais_proximo = -1
        menor_distancia = float('inf')

        for proxima_cidade in range(num_cidades):
            if not visitadas[proxima_cidade]:
                distancia = matriz_adjacencia[cidade_atual][proxima_cidade]
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    vizinho_mais_proximo = proxima_cidade
        
        if vizinho_mais_proximo != -1:
            caminho.append(vizinho_mais_proximo)
            visitadas[vizinho_mais_proximo] = True
            custo_total += menor_distancia
            cidade_atual = vizinho_mais_proximo
        else:
            break
            
    if caminho:
        custo_total += matriz_adjacencia[caminho[-1]][caminho[0]]
        caminho.append(caminho[0])

    return caminho, custo_total

def executar_aproximativo(nome_arquivo):

    matriz = ler_matriz_adjacencia(nome_arquivo)
    
    start_time = time.time()
    caminho, custo = algoritmo_vizinho_mais_proximo(matriz)
    end_time = time.time()
    tempo_execucao = end_time - start_time
    
    return caminho, custo, tempo_execucao
