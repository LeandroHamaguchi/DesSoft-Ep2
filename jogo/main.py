import sys
sys.path.append('funções')

from define_posicoes import define_posicoes
from faz_jogada import faz_jogada
from navios_afundados import afundados
from posicao_valida import posicao_valida
from posiciona_frota import posiciona_frota
from preenche_frota import preenche_frota
from monta_tabuleiros import monta_tabuleiros

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
info_frota = {
    "porta-aviões": {'tamanho': 4, 'quantidade': 1},
    "navio-tanque": {'tamanho': 3, 'quantidade': 2},
    "contratorpedeiro": {'tamanho': 2, 'quantidade': 3},
    "submarino": {'tamanho': 1, 'quantidade': 4},
}
'''
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
                
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
        i+=1

print(frota)
'''
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
    tabuleiro_oponete = []
    if tabuleiro_oponete == []:
        tabuleiro_oponete = posiciona_frota(frota_oponente)
    else:
        pass
    coordenadas_atacadas_anteriormente = []
    linha = int(input("Em qual linha você deseja atacar?"))
    while linha > 9 or linha < 0:
        print("Linha inválida!")
        linha = int(input("Em qual linha você deseja atacar?"))
    coluna = int(input("Em qual coluna você deseja atacar?"))
    while coluna > 9 or coluna < 0:
        print("Coluna inválida!")
        coluna = int(input("Em qual Coluna você deseja atacar?"))
    while [linha, coluna] in coordenadas_atacadas_anteriormente:
        print ("A poisção linha LINHA e coluna COLUNA já foi informada anteriormente")
        linha = int(input("Em qual linha você deseja atacar?"))
        while linha > 9 or linha < 0:
            print("Linha inválida!")
            linha = int(input("Em qual linha você deseja atacar?"))
        coluna = int(input("Em qual coluna você deseja atacar?"))
        while coluna > 9 or coluna < 0:
            print("Coluna inválida!")
            coluna = int(input("Em qual Coluna você deseja atacar?"))
    coordenadas_atacadas_anteriormente.append([linha, coluna])

    
    
    










    

    

