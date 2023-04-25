from funções.define_posicoes import define_posicoes
from funções.navios_afundados import afundados
from funções.posicao_valida import posicao_valida
from funções.posiciona_frota import posiciona_frota

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for nome_navio, posicao_navios in frota.items():
    for navio in range(len(posicao_navios)):
        tamanho = len(navio)
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {len(tamanho)};")

        while posicao_valida == False:
            linha = int(input("Linha > "))
            coluna = int(input("Coluna > "))
            if len(navio) == 1:
                pass
            else:
                orientacao = int(input("Orientação: [1]Vertical [2]Horizontal > "))
            posicao_valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if posicao_valida == True:
                break
            else:
                print("Esta posição não está válida!")
        
        posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)
        frota[nome_navio].append(posicao_navio)
        

