# Parte 2 (Verifica se a posição definida é válida)
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

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if linha > 10 or coluna > 10:
        return False
    elif orientacao == 'horizontal':
        if coluna + tamanho > 10:
            return False
    elif orientacao == 'vertical':
        if linha + tamanho > 10:
            return False
        
    if frota == {}:
        return True
    else:
        for navio in frota.values():
            for i in range(len(navio)):
                for posicao in navio[i]:
                    for posicao_novo in novo_navio:
                        if posicao == posicao_novo:
                            return False

    return True