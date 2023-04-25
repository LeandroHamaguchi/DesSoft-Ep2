def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    comeco = [linha,coluna]



    i = 0
    posicao_navio = [0]*tamanho
    while i < tamanho:
        if orientacao == "vertical":
            posicao_navio[i] = [linha + i, coluna]
        else:
            posicao_navio[i] = [linha, coluna + i]
        i+=1
        
    if nome in frota.keys():
        tamanho_chave = len(frota[str(nome)])
        frota[str(nome)].append(posicao_navio)
    else:
        frota[str(nome)] = [posicao_navio]

    return frota

    

