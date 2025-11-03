# algoritmo_insercao.py
import time
from le_matriz import ler_matriz_adjacencia

def algoritmo_heuristica_insercao(matriz_adjacencia):
    """Implementa a Heurística de Inserção para o PCV."""
    num_cidades = len(matriz_adjacencia)
    
    if num_cidades < 3:
        # Casos triviais ou insuficientes para um ciclo não-trivial
        if num_cidades == 1:
            return [0, 0], 0
        elif num_cidades == 2:
            custo = matriz_adjacencia[0][1] + matriz_adjacencia[1][0]
            return [0, 1, 0], custo
        
    # 1. Inicia com um ciclo de 2 cidades (0 e o vizinho mais próximo de 0)
    cidade_inicial = 0
    cidades_nao_visitadas = list(range(1, num_cidades))
    
    # Encontra o vizinho mais próximo de 0 para iniciar
    segunda_cidade = -1
    menor_distancia = float('inf')
    for cidade in cidades_nao_visitadas:
        if matriz_adjacencia[cidade_inicial][cidade] < menor_distancia:
            menor_distancia = matriz_adjacencia[cidade_inicial][cidade]
            segunda_cidade = cidade

    caminho = [cidade_inicial, segunda_cidade, cidade_inicial]
    cidades_nao_visitadas.remove(segunda_cidade)

    # 2. Insere as cidades restantes
    while cidades_nao_visitadas:
        # Encontrar a próxima cidade 'r' a ser inserida (a primeira não visitada)
        r = cidades_nao_visitadas[0]
        
        melhor_custo_adicional = float('inf')
        melhor_posicao_insercao = -1
        
        # Encontra a melhor aresta (i, j) no ciclo atual para inserir 'r'
        for i in range(len(caminho) - 1):
            i_cidade = caminho[i]
            j_cidade = caminho[i+1]
            
            # Custo: custo_r_i + custo_r_j - custo_i_j
            custo_adicional = (matriz_adjacencia[i_cidade][r] + 
                               matriz_adjacencia[r][j_cidade] - 
                               matriz_adjacencia[i_cidade][j_cidade])
            
            if custo_adicional < melhor_custo_adicional:
                melhor_custo_adicional = custo_adicional
                melhor_posicao_insercao = i + 1 # Posição para inserir 'r' entre i e j

        # Insere 'r' na melhor posição
        caminho.insert(melhor_posicao_insercao, r)
        cidades_nao_visitadas.remove(r)

    # 3. Calcula o custo total do ciclo final
    custo_total = 0
    for i in range(len(caminho) - 1):
        custo_total += matriz_adjacencia[caminho[i]][caminho[i+1]]

    return caminho, custo_total

def executar_insercao(nome_arquivo):
    """Executa o algoritmo de inserção e mede o tempo."""
    matriz = ler_matriz_adjacencia(nome_arquivo)
    
    start_time = time.time()
    caminho, custo = algoritmo_heuristica_insercao(matriz)
    end_time = time.time()
    tempo_execucao = end_time - start_time
    
    return caminho, custo, tempo_execucao