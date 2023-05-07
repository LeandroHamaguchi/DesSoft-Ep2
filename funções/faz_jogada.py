# Parte 5 (A função recebe o tabuleiro de quem está sendo atacado e as coordenadas que vão ser atacadas, e depois retorna o tabuleiro após o ataque)
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro 
