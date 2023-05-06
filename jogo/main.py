import sys
sys.path.append('funções')

from define_posicoes import define_posicoes
from faz_jogada import faz_jogada
from navios_afundados import afundados
from posicao_valida import posicao_valida
from posiciona_frota import posiciona_frota
from preenche_frota import preenche_frota

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