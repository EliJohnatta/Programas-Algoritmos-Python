from maquina import Maquina

maquina = Maquina()

while True:
    entrada_inicial = maquina.exibirInterfaceInicialUsuario()
    if entrada_inicial == 1:
        print('\n')
        escolha_produto = maquina.listarProdutos()
        produto_escolhido = maquina.verificarDisponibilidadeEstoque(escolha_produto)
        if produto_escolhido == 9 or produto_escolhido == 0:
            print('\n')
            pass
        else:
            maquina.comprarProduto(produto_escolhido)
    elif entrada_inicial == 2:
        print('\n')
        maquina.vericarSenhaAdministrativa()
        escolha_funcao = maquina.listarFuncionalidadesAdministrativas()
        if escolha_funcao == 1:
            print('Valor em Vendas: R$ {vendas}.00\n'.format(vendas = maquina.receitaVendas))
        elif escolha_funcao == 0:
            print('\n')
            pass
    elif entrada_inicial == 0:
        break
