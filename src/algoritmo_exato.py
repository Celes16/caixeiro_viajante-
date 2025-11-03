
import itertools
import time
from le_matriz import ler_matriz_adjacencia

def algoritmo_exato_forca_bruta(matriz_adjacencia):

    num_cidades = len(matriz_adjacencia)
    cidade_inicial = 0
    cidades = list(range(num_cidades))
    cidades_internas = cidades[1:] 
    
    melhor_caminho = []
    menor_custo = float('inf')

    for permutacao in itertools.permutations(cidades_internas):
        caminho_atual = [cidade_inicial] + list(permutacao) + [cidade_inicial]
        custo_atual = 0

        for i in range(num_cidades):
            origem = caminho_atual[i]
            destino = caminho_atual[i+1]
            custo_atual += matriz_adjacencia[origem][destino]
        
        if custo_atual < menor_custo:
            menor_custo = custo_atual
            melhor_caminho = caminho_atual

    return melhor_caminho, menor_custo

def executar_exato(nome_arquivo):

    matriz = ler_matriz_adjacencia(nome_arquivo)
    
    num_cidades = len(matriz)
    if num_cidades > 10:
        return "N/A", "N/A", "Timeout"

    start_time = time.time()
    caminho, custo = algoritmo_exato_forca_bruta(matriz)
    end_time = time.time()
    tempo_execucao = end_time - start_time
    
    return caminho, custo, tempo_execucao
