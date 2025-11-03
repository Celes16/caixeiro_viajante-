# main.py
import os
import re
from algoritmo_aproximativo import executar_aproximativo
from algoritmo_exato import executar_exato
from algoritmo_insercao import executar_insercao # NOVA IMPORTAÇÃO
from le_matriz import ler_matriz_adjacencia

def extrair_custo_otimo(nome_arquivo):
    """Extrai o custo ótimo de um nome de arquivo no formato 'tsp_xxx.txt'."""
    try:
        match = re.search(r'_(\d+)\.txt$', nome_arquivo)
        if match:
            return int(match.group(1))
    except (ValueError, TypeError):
        return None
    return None

def processar_instancia(caminho_completo_arquivo):
    """Processa uma única instância TSP e imprime os resultados."""
    nome_arquivo_simples = os.path.basename(caminho_completo_arquivo)
    print(f"--- Processando instância: {nome_arquivo_simples} ---")
    
# --- NOVO TRECHO: Leitura para Contagem de Vértices ---
    matriz_temp = ler_matriz_adjacencia(caminho_completo_arquivo)
    num_cidades = len(matriz_temp)
    print(f"Número de Cidades (Vértices): {num_cidades}")
    print("-" * 30)
    # ------------------------------------------------------

    custo_otimo = extrair_custo_otimo(nome_arquivo_simples)
    if custo_otimo is None:
        print("Aviso: Não foi possível extrair o custo ótimo do nome do arquivo.")


    # --- Algoritmo Aproximativo (Vizinho Mais Próximo) ---
    caminho_vmp, custo_vmp, tempo_vmp = executar_aproximativo(caminho_completo_arquivo)
    
    print("\n[Algoritmo Aproximativo (Vizinho Mais Próximo)]")
    print(f"Tempo de execução: {tempo_vmp:.6f} segundos")
    print(f"Custo da solução: {custo_vmp}")
    if custo_otimo is not None:
        qualidade_vmp = (custo_vmp / custo_otimo) * 100
        print(f"Qualidade da solução (em relação ao ótimo): {qualidade_vmp:.2f}%")
    print("-" * 30)

    # --- Algoritmo Aproximativo (Heurística de Inserção) ---
    caminho_ins, custo_ins, tempo_ins = executar_insercao(caminho_completo_arquivo)
    
    print("\n[Algoritmo Aproximativo (Heurística de Inserção)]")
    print(f"Tempo de execução: {tempo_ins:.6f} segundos")
    print(f"Custo da solução: {custo_ins}")
    if custo_otimo is not None:
        qualidade_ins = (custo_ins / custo_otimo) * 100
        print(f"Qualidade da solução (em relação ao ótimo): {qualidade_ins:.2f}%")
    print("-" * 30)

    # --- Algoritmo Exato (Força Bruta) ---
    matriz_exato = ler_matriz_adjacencia(caminho_completo_arquivo)
    if len(matriz_exato) > 10:
        print("\n[Algoritmo Exato (Força Bruta)]")
        print("Não foi possível esperar o término: Muitas cidades para Força Bruta.")
    else:
        caminho_exato, custo_exato, tempo_exato = executar_exato(caminho_completo_arquivo)
        print("\n[Algoritmo Exato (Força Bruta)]")
        print(f"Tempo de execução: {tempo_exato:.6f} segundos")
        print(f"Custo da solução: {custo_exato}")
        if custo_otimo is not None:
            print(f"Custo da solução: {custo_exato} (esperado: {custo_otimo})")
            if custo_exato != custo_otimo:
                print("Aviso: O custo ótimo obtido não corresponde ao custo do arquivo. Verifique a instância.")
    print("-" * 30)


# --- Execução Principal ---
if __name__ == "__main__":
    
    # Lista de arquivos a serem processados (atualizada conforme sua descrição)
    arquivos_instancias = ["tsp1_253.txt", "tsp2_1248.txt", "tsp3_1194.txt", "tsp4_7013.txt", "tsp5_27603.txt"]

    # Constrói o caminho para cada arquivo no diretório pai
    for nome_arquivo in arquivos_instancias:
        caminho_completo = os.path.join(os.path.dirname(os.path.dirname(__file__)), nome_arquivo)
        
        if os.path.exists(caminho_completo):
            processar_instancia(caminho_completo)
        else:
            print(f"Erro: O arquivo '{caminho_completo}' não foi encontrado. Verifique se a lista está correta e se o arquivo está no diretório pai.")
