import sys
import random
sys.path.append('funções')

from define_posicoes import define_posicoes
from faz_jogada import faz_jogada
from navios_afundados import afundados
from posicao_valida import posicao_valida
from posiciona_frota import posiciona_frota
from preenche_frota import preenche_frota
from monta_tabuleiros import monta_tabuleiros

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

jogando = input(str('Deseja jogar?[True/False]:'))

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
            orientacao = str(input('Orientação [1 = Vertical/ 2 = Horizontal]:'))

            if posicao_valida(frota,linha,coluna,orientacao,tamanho) == False:
                print('Deu errado, escolhe de novo')
            elif posicao_valida(frota,linha,coluna,orientacao,tamanho) == True:
                frota = preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
                natureza = 'valida'
        
    tabuleiro_jogador = posiciona_frota(frota)
    print(tabuleiro_jogador)

    tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)

    partida_acontecendo = True
    while partida_acontecendo == True:
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

        faz_jogada(tabuleiro_oponente, linha_ataque_jogador, coluna_ataque_jogador)

        navios_afundados = afundados(frota, tabuleiro_oponente)
        if navios_afundados == 10:
            print ("'Parabéns! Você derrubou todos os navios do seu oponente!'")
            jogando = False
            break
        
        coordenadas_atacadas_oponente = []
        linha = random.randint(0, 9)
        coluna = random.randit(0, 9)
        while [linha, coluna] in coordenadas_atacadas_oponente:
            linha = random.randint(0, 9)
            coluna = random.randit(0, 9)
        coordenadas_atacadas_oponente.append([linha, coluna])
        faz_jogada(tabuleiro_jogador, linha, coluna)

        afundados(frota, tabuleiro_jogador)
        if navios_afundados == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
            break
    
    










    

    



'''
info_frota = {
    "porta-aviões": {'tamanho': 4, 'quantidade': 1},
    "navio-tanque": {'tamanho': 3, 'quantidade': 2},
    "contratorpedeiro": {'tamanho': 2, 'quantidade': 3},
    "submarino": {'tamanho': 1, 'quantidade': 4},
}

for nome_navio, dict_info in info_frota.items():
        i = 0
        while i < dict_info['quantidade']:
            validando = False
            tamanho = dict_info['tamanho']
            while validando == False:
                print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {dict_info['tamanho']}")
                linha = int(input('Linha: '))
                coluna = int(input('Coluna: '))
                if nome_navio != "submarino":
                    orientacao = int(input('Orientação [1]Vertical [2]Horizontal: '))
                    if orientacao == 1:
                        orientacao = 'vertical'
                    elif orientacao == 2:
                        orientacao = 'horizontal'
                else:
                    orientacao = 'vertical'
                validando = posicao_valida(frota, linha, coluna, orientacao, tamanho)
                if validando == False:
                    print("Esta posição não está válida!")
                    
        frota_jogador = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
        i+=1
    print(frota_jogador)
    tabuleiro_jogador = posiciona_frota(frota_jogador)'''

