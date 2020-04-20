
def encerrar_jogo():
    print('Obrigado por jogar ^_^')

def verificacao_status_jogo_para_jogador1(lista_de_jogadas):
    if lista_de_jogadas[1] == 'X' and lista_de_jogadas[2] == 'X' and lista_de_jogadas[3] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[4] == 'X' and lista_de_jogadas[5] == 'X' and lista_de_jogadas[6] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[7] == 'X' and lista_de_jogadas[8] == 'X' and lista_de_jogadas[9] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[1] == 'X' and lista_de_jogadas[4] == 'X' and lista_de_jogadas[7] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[2] == 'X' and lista_de_jogadas[5] == 'X' and lista_de_jogadas[8] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[3] == 'X' and lista_de_jogadas[6] == 'X' and lista_de_jogadas[9] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[1] == 'X' and lista_de_jogadas[5] == 'X' and lista_de_jogadas[9] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[3] == 'X' and lista_de_jogadas[5] == 'X' and lista_de_jogadas[7] == 'X':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[0] == 5:
        situacao_jogo = 'empate'
    else: 
        situacao_jogo = 'continue'
    return situacao_jogo

def verificacao_status_jogo_para_jogador2(lista_de_jogadas):
    if lista_de_jogadas[1] == 'O' and lista_de_jogadas[2] == 'O' and lista_de_jogadas[3] == 'O':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[4] == 'O' and lista_de_jogadas[5] == 'O' and lista_de_jogadas[6] == 'O':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[7] == 'O' and lista_de_jogadas[8] == 'O' and lista_de_jogadas[9] == 'O':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[1] == 'O' and lista_de_jogadas[4] == 'O' and lista_de_jogadas[7] == 'O':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[2] == 'O' and lista_de_jogadas[5] == 'O' and lista_de_jogadas[8] == 'O':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[3] == 'O' and lista_de_jogadas[6] == 'O' and lista_de_jogadas[9] == 'O':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[1] == 'O' and lista_de_jogadas[5] == 'O' and lista_de_jogadas[9] == 'O':
        situacao_jogo = 'termine'
    elif lista_de_jogadas[3] == 'O' and lista_de_jogadas[5] == 'O' and lista_de_jogadas[7] == 'O':
        situacao_jogo = 'termine'
    else: 
        situacao_jogo = 'continue'
    return situacao_jogo


def inserir_jogada_jogador1(posicao1, lista_de_jogadas):
    if lista_de_jogadas[posicao1] != 'O' and lista_de_jogadas[posicao1] != 'X':
        lista_de_jogadas[posicao1] = 'X'
        lista_de_jogadas[10] = True
    else:
        lista_de_jogadas[10] = False
    return lista_de_jogadas[10]

def inserir_jogada_jogador2(posicao2, lista_de_jogadas):
    if lista_de_jogadas[posicao2] != 'X' and lista_de_jogadas[posicao2] != 'O':
        lista_de_jogadas[posicao2] = 'O'
        lista_de_jogadas[10] = True
    else:
        lista_de_jogadas[10] = False
    return lista_de_jogadas[10]

def convocar_jogador1():
    entrada_jogador1 = int(input('Jogador1, escolha uma posição válida no tabuleiro: '))
    return entrada_jogador1

def convocar_jogador2():
    entrada_jogador2 = int(input('Jogador2, escolha uma posição válida no tabuleiro: '))
    return entrada_jogador2

def imprimir_tabuleiro(l):
    print ('_{a}_|_{b}_|_{c}_\n_{d}_|_{e}_|_{f}_\n {g} | {h} | {i} \n'.format(a = l[1], b = l[2], c = l[3],
    d = l[4], e = l[5], f = l[6], g = l[7], h = l[8], i = l[9]),)

def iniciar_logica_jogo():
    #jogadas[0] flag p/ identificar a rodada atual
    #jogadas[10] flag p/ saber se a jogada foi realizada com sucesso
    jogadas = [1, '1', '2', '3', '4', '5', '6', '7', '8', '9', True]
    #Tabuleiro na forma inicial
    imprimir_tabuleiro(jogadas)

    while jogadas[0] <= 5:
        print('{num_rodada}° Rodada'.format(num_rodada = jogadas[0]))
        entrada_jogador1 = convocar_jogador1()
        jogada_jogador1 = inserir_jogada_jogador1(entrada_jogador1,jogadas)
        while jogada_jogador1 == False:
            print('Posição inválida °_°, insira uma correta!')
            entrada_jogador1 = convocar_jogador1()
            jogada_jogador1 = inserir_jogada_jogador1(entrada_jogador1,jogadas)
        if jogadas[0] >= 3:
            situacao = verificacao_status_jogo_para_jogador1(jogadas)
            if situacao == 'termine':
                print('Jogador1 foi o vencedor!')
                imprimir_tabuleiro(jogadas)
                break
            elif situacao == 'empate':
                print('Jogo empatado!')
                imprimir_tabuleiro(jogadas)
                break
            else:
                imprimir_tabuleiro(jogadas)
        elif jogadas[0] < 3:
            imprimir_tabuleiro(jogadas)


        entrada_jogador2 = convocar_jogador2()
        jogada_jogador2 = inserir_jogada_jogador2(entrada_jogador2,jogadas)
        while jogada_jogador2 == False:
            print('Posição inválida °_°, insira uma correta!')
            entrada_jogador2 = convocar_jogador2()
            jogada_jogador2 = inserir_jogada_jogador2(entrada_jogador2,jogadas)
        if jogadas[0] >= 3:
            situacao = verificacao_status_jogo_para_jogador2(jogadas)
            if situacao == 'termine':
                print('Jogador2 foi o vencedor!')
                imprimir_tabuleiro(jogadas)
                break
            else:
                imprimir_tabuleiro(jogadas)
        elif jogadas[0] < 3:
            imprimir_tabuleiro(jogadas)
        jogadas[0] += 1

def iniciar_jogo_da_velha():
    flag_continuar_encerrar = 0
    while flag_continuar_encerrar == 0:
        iniciar_logica_jogo()
        flag_continuar_encerrar = int(input('Deseja jogar novamente?\nDigite 0 para isso, caso deseje sair digite 1.\n'))
        if flag_continuar_encerrar == 1:
            encerrar_jogo()

iniciar_jogo_da_velha()