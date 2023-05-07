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