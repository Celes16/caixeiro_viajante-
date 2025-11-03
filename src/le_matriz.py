
import sys

def ler_matriz_adjacencia(nome_arquivo):

    matriz = []
    try:
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                valores = linha.strip().split()
                if valores:
                    linha_valores = [int(v) for v in valores]
                    matriz.append(linha_valores)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)
    except ValueError:
        print(f"Erro: O arquivo '{nome_arquivo}' contém dados inválidos. Certifique-se de que são apenas números.")
        sys.exit(1)
    
    if not matriz:
        print(f"Erro: O arquivo '{nome_arquivo}' está vazio.")
        sys.exit(1)

    return matriz
