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

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome in frota.keys():
        frota[str(nome)].append(posicao_navio)
    else:
        frota[str(nome)] = [posicao_navio]

    return frota