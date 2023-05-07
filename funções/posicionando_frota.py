lista_navios = ['porta-aviões','navio-tanque','navio-tanque','contratorpedeiro','contratorpedeiro','contratorpedeiro','submarino','submarino','submarino','submarino']
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

def posiciona_frota(frota):
    tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for navios in frota.values():
        for navio in navios:
            for linha_coluna in navio:
              i = linha_coluna[0]
              j = linha_coluna[1]
              tabuleiro[i][j] = 1

    print(tabuleiro)
    return tabuleiro
def define_posicoes(linha, coluna, orientacao, tamanho):
    i = 0
    posicao_navio = [0]*tamanho
    while i < tamanho:
        if orientacao == "1":
            posicao_navio[i] = [linha + i, coluna]
        else:
            posicao_navio[i] = [linha, coluna + i]
        i+=1
        
    return posicao_navio
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if linha > 10 or coluna > 10:
        return False
    elif orientacao == '2':
        if coluna + tamanho > 10:
            return False
    elif orientacao == '1':
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
def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    i = 0
    posicao_navio = [0]*tamanho
    while i < tamanho:
        if orientacao == "vertical":
            posicao_navio[i] = [linha + i, coluna]
        else:
            posicao_navio[i] = [linha, coluna + i]
        i+=1      
    if nome in frota.keys():
        frota[str(nome)].append(posicao_navio)
    else:
        frota[str(nome)] = [posicao_navio]
    return frota 


for i in lista_navios:
    natureza = 'invalida'
    while natureza != 'valida':
        if i == 'porta-aviões':
            print(f'Insira as informações referentes ao navio {i} que possui tamanho 4')
            navio = 'porta-aviões'
            tamanho = 4
        elif i == 'navio-tanque':
            print(f'Insira as informações referentes ao navio {i} que possui tamanho 3')
            navio = 'navio-tanque'
            tamanho = 3
        elif i == 'contratorpedeiro':
            print(f'Insira as informações referentes ao navio {i} que possui tamanho 2')
            navio = 'contratorpedeiro'
            tamanho = 2
        elif i == 'submarino':
            print(f'Insira as informações referentes ao navio {i} que possui tamanho 1')
            navio = 'submarino'
            tamanho = 1
        
        linha = int(input('Linha:'))
        coluna = int(input('Coluna:'))
        orientacao = str(input('Orientação [1 = Vertical/ 2 = Horizontal]:'))

        if posicao_valida(frota,linha,coluna,orientacao,tamanho) == False:
            print('Deu errado, escolhe de novo')
        elif posicao_valida(frota,linha,coluna,orientacao,tamanho) == True:
            preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
            natureza = 'valida'
    
tabueleiro_jogador = posiciona_frota(frota)

print(tabueleiro_jogador)

