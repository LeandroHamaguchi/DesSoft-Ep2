def define_posicoes(linha, coluna, orientacao, tamanho):
    i = 0
    posicao_navio = [0]*tamanho
    while i < tamanho:
        if orientacao == "vertical":
            posicao_navio[i] = [linha , coluna + 1]
        else:
            posicao_navio[i] = [linha + 1, coluna]
        i+=1
        
    return posicao_navio

# Parte 3 (Armazena as posições de todas as embarcações em um dicionário chamado frota)
def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome in frota.keys():
        frota[str(nome)].append(posicao_navio)
    else:
        frota[str(nome)] = [posicao_navio]

    return frota

