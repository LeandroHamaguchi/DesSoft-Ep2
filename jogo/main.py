import random

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

# Parte 2 (Verifica se a posição definida é válida)

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

# Parte 3 (Armazena as posições de todas as embarcações em um dicionário chamado frota)
def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome in frota.keys():
        frota[str(nome)].append(posicao_navio)
    else:
        frota[str(nome)] = [posicao_navio]

    return frota


# Parte 4 (A função recebe a frota e posiciona ela no tabuleiro)
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

    return tabuleiro


# Parte 5 (A função recebe o tabuleiro de quem está sendo atacado e as coordenadas que vão ser atacadas, e depois retorna o tabuleiro após o ataque)
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro


# Parte 6 (A função recebe a frota e o tabuleiro de quem foi atacado e retorna quantos navios foram afundados)
def afundados(frota, tabuleiro):
    lista_posicoes = []
    lista_x = 0
    afundados = 0

    for navio in frota.values():
        for i in range(len(navio)):
            lista_posicoes.append(navio[i])

    for navios in lista_posicoes:
        lista_x = 0
        for posicoes in navios:
            if tabuleiro[posicoes[0]][posicoes[1]] == 'X':
                lista_x += 1
                if lista_x == len(navios):
                    afundados += 1
    
    return afundados


# Parte 7 (Monta os tabuleiros iniciais do jogo)
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
 

lista_navios = ['porta-aviões','navio-tanque','navio-tanque','contratorpedeiro','contratorpedeiro','contratorpedeiro','submarino','submarino','submarino','submarino']

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

jogando = True
coordenadas_atacadas_oponente = []
partida_acontecendo = True

while jogando == True:
    tabuleiro_oponente = []
    if tabuleiro_oponente == []:
        tabuleiro_oponente = posiciona_frota(frota_oponente)
    else:
        pass
    
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
            if i != 'submarino':
                orientacao = int(input('Orientação [1 = Vertical/ 2 = Horizontal]:'))
                while orientacao not in [1,2]:
                    orientacao = int(input('Orientação [1 = Vertical/ 2 = Horizontal]:'))
            else:
                orientacao=1
            
            if orientacao==1:
                orientacao='vertical'
            
            if orientacao ==2:
                orientacao='horizontal'

            if posicao_valida(frota,linha,coluna,orientacao,tamanho) == False:
                print('Deu errado, escolha de novo')
            elif posicao_valida(frota,linha,coluna,orientacao,tamanho) == True:
                frota = preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
                natureza = 'valida'
       
    tabuleiro_jogador = posiciona_frota(frota)
    
    tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(tabuleiros)


    while partida_acontecendo:
        print(tabuleiros)
        coordenadas_atacadas_anteriormente = []
        linha_ataque_jogador = int(input("Em qual linha você deseja atacar?"))
        while linha_ataque_jogador> 9 or linha_ataque_jogador < 0:
            print("Linha inválida!")
            linha_ataque_jogador = int(input("Em qual linha você deseja atacar?"))
        coluna_ataque_jogador = int(input("Em qual coluna você deseja atacar?"))
        while coluna_ataque_jogador > 9 or coluna_ataque_jogador < 0:
            print("Coluna inválida!")
            coluna_ataque_jogador = int(input("Em qual Coluna você deseja atacar?"))
        while [linha_ataque_jogador, coluna_ataque_jogador] in coordenadas_atacadas_anteriormente:
            print ("A poisção linha LINHA e coluna COLUNA já foi informada anteriormente!")
            linha_ataque_jogador = int(input("Em qual linha você deseja atacar?"))
            while linha_ataque_jogador > 9 or linha_ataque_jogador < 0:
                print("Linha inválida!")
                linha_ataque_jogador = int(input("Em qual linha você deseja atacar?"))
            coluna_ataque_jogador = int(input("Em qual coluna você deseja atacar?"))
            while coluna_ataque_jogador > 9 or coluna_ataque_jogador < 0:
                print("Coluna inválida!")
                coluna_ataque_jogador = int(input("Em qual Coluna você deseja atacar?"))
        coordenadas_atacadas_anteriormente.append([linha_ataque_jogador, coluna_ataque_jogador])

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque_jogador, coluna_ataque_jogador)
        
        

        navios_afundados = afundados(frota_oponente, tabuleiro_oponente)
        
            
        linha_ataque_oponente = random.randint(0, 9)
        coluna_ataque_oponente = random.randint(0, 9)
        while [linha_ataque_oponente, coluna_ataque_oponente] in coordenadas_atacadas_oponente:
            linha_ataque_oponente = random.randint(0, 9)
            coluna_ataque_oponente = random.randint(0, 9)
        coordenadas_atacadas_oponente.append([linha_ataque_oponente, coluna_ataque_oponente])
        print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_ataque_oponente,coluna_ataque_oponente))
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_ataque_oponente, coluna_ataque_oponente)
        tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente) 

        navios_afundados_jogador = afundados(frota, tabuleiro_jogador)
        if navios_afundados == 10:
            print ("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False
            partida_acontecendo=False
            break
        if navios_afundados_jogador == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            partida_acontecendo = False
            jogando = False
            break