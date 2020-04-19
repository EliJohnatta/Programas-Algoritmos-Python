from maquina import Maquina

maquina = Maquina()
copia = maquina

while True:
    entrada_inicial = maquina.exibirInterfaceInicialUsuario()
    if entrada_inicial == 1:
        print('\n')
        escolha_produto = maquina.listarProdutos()
        produto_escolhido = maquina.verificarDisponibilidadeEstoque(escolha_produto)
        if produto_escolhido == 9 or produto_escolhido == 0:
            pass
        else:
            maquina.comprarProduto(produto_escolhido, copia)
    elif entrada_inicial == 0:
        break