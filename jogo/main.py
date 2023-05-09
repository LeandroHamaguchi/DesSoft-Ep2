import sys
import random
random.seed(2)
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

jogando = True

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
                orientacao = str(input('Orientação [1 = Vertical/ 2 = Horizontal]:'))
            else:
                orientacao=1

            if posicao_valida(frota,linha,coluna,orientacao,tamanho) == False:
                print('Deu errado, escolha de novo')
            elif posicao_valida(frota,linha,coluna,orientacao,tamanho) == True:
                frota = preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
                natureza = 'valida'
       
    tabuleiro_jogador = posiciona_frota(frota)
    
    tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(tabuleiros)

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

        tabuleiro_novo_oponente = faz_jogada(tabuleiro_oponente, linha_ataque_jogador, coluna_ataque_jogador)
        tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_novo_oponente)
        print(tabuleiros)

        navios_afundados = afundados(frota_oponente, tabuleiro_novo_oponente)
        if navios_afundados == 10:
            print ("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False
            break
        
        coordenadas_atacadas_oponente = []
        linha_ataque_oponente = random.randint(0, 9)
        coluna_ataque_oponente = random.randint(0, 9)
        while [linha_ataque_oponente, coluna_ataque_oponente] in coordenadas_atacadas_oponente:
            linha_ataque_oponente = random.randint(0, 9)
            coluna_ataque_oponente = random.randint(0, 9)
        coordenadas_atacadas_oponente.append([linha_ataque_oponente, coluna_ataque_oponente])
        print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_ataque_oponente,coluna_ataque_oponente))
        tabuleiro_novo_jogador = faz_jogada(tabuleiro_jogador, linha_ataque_oponente, coluna_ataque_oponente)
        tabuleiros = monta_tabuleiros(tabuleiro_novo_jogador, tabuleiro_novo_oponente) 
        print(tabuleiros)

        navios_afundados = afundados(frota, tabuleiro_novo_jogador)
        if navios_afundados == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
            break