# Parte 1 (Define a posição do navio no tabuleiro)
def define_posicoes(linha, coluna, orientacao, tamanho):
    i = 0
    posicao_navio = [0]*tamanho
    while i < tamanho:
        if orientacao == "vertical":
            posicao_navio[i] = [linha + i, coluna]
        else:
            posicao_navio[i] = [linha, coluna + i]
        i+=1

    return posicao_navio