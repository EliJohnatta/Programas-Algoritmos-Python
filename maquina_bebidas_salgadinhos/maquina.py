from bebida import Bebida
from salgadinho import Salgadinho

#Máquina idealizada: 6 Seções com 4 divisorias cada, sendo que cada divisoria suporta 8 produtos
class Maquina(object):

    def __init__(self):
        self.cheetos_cheddar = Salgadinho('Cheetos', 'Cheddar', 2, 16, '51 g')
        self.cheetos_parmesao = Salgadinho('Cheetos', 'Parmesão', 2, 16, '51 g')
        self.cheetos_queijo = Salgadinho('Cheetos', 'Queijo', 2, 16, '51 g')
        self.cheetos_requeijao = Salgadinho('Cheetos', 'Requeijão', 2, 16, '51 g')
        self.doritos = Salgadinho('Doritos', 'Queijo Nacho', 5, 32, '96 g')
        self.coca_cola = Bebida('Coca-Cola', 'Cola', 5, 32, '350 ml')
        self.sprite = Bebida('Sprit', 'Limão', 4, 32, '350 ml')
        self.guarana = Bebida('Guaraná Antarctica', 'Guaraná', 4, 32, '350 ml')
        self.troco = {'qtdMoedasUmReal':10}
        self.receita_lucrativa = 0

    def exibirInterfaceInicialUsuario(self):
        while True:
            try:
                print('Seja Bem-Vindo! Selecione umas das opções abaixo:')
                resposta = int(input('1 - Comprar Produto\n0 - Sair\n'))
            except ValueError:
                print('ERRO, informe somente números que correspondem as opções!\n')
            else:
                while True:
                    try:
                        while resposta != 1 and resposta != 0:
                            print('Número digitado INCORRETO, tente mais uma vez!\n')
                            resposta = int(input('1 - Comprar Produto\n0 - Sair\n'))
                    except ValueError:
                        print('ERRO, informe somente os números que correspondem as opções!\n')
                    else:
                        return resposta

    def listarProdutos(self):
        while True:
            try:
                resposta = int(input('Lista de Produtos:\n1 - {p1}\n2 - {p2}\n3 - {p3}\n4 - {p4}\n5 - {p5}\n6 - {p6}\n7 - {p7}\n8 - {p8}\n0 - Cancelar\nQual deseja?\n'.format(p1 = self.cheetos_cheddar,
                p2 = self.cheetos_parmesao, p3 = self.cheetos_queijo, p4 = self.cheetos_requeijao, p5 = self.doritos, p6 = self.coca_cola, p7 = self.sprite, p8 = self.guarana)))
            except ValueError:
                print('ERRO, informe somente números que correspondem as opções!\n')
            else:
                while True:
                    try:
                        while resposta < 0 or resposta > 8:
                            print('Número digitado INCORRETO, tente mais uma vez!\n')
                            resposta = int(input('Lista de Produtos:\n1 - {p1}\n2 - {p2}\n3 - {p3}\n4 - {p4}\n5 - {p5}\n6 - {p6}\n7 - {p7}\n8 - {p8}\n0 - Cancelar\nQual deseja?\n'.format(p1 = self.cheetos_cheddar,
                            p2 = self.cheetos_parmesao, p3 = self.cheetos_queijo, p4 = self.cheetos_requeijao, p5 = self.doritos, p6 = self.coca_cola, p7 = self.sprite, p8 = self.guarana)))
                    except ValueError:
                        print('ERRO, informe somente os números que correspondem as opções!\n')
                    else:
                        return resposta
                    
    def verificarDisponibilidadeEstoque(self, opcao):
        if opcao == 1 and self.cheetos_cheddar.getQtdEstoque() != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_cheddar.getNome(),
            sabor = self.cheetos_cheddar.getSabor()))
            return self.cheetos_cheddar
        elif opcao == 2 and self.cheetos_parmesao.getQtdEstoque() != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_parmesao.getNome(),
            sabor = self.cheetos_parmesao.getSabor()))
            return self.cheetos_parmesao
        elif opcao == 3 and self.cheetos_queijo.getQtdEstoque() != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_queijo.getNome(),
            sabor = self.cheetos_queijo.getSabor()))
            return self.cheetos_queijo
        elif opcao == 4 and self.cheetos_requeijao.getQtdEstoque() != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_requeijao.getNome(),
            sabor = self.cheetos_requeijao.getSabor()))
            return self.cheetos_requeijao
        elif opcao == 5 and self.doritos.getQtdEstoque() != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.doritos.getNome(),
            sabor = self.doritos.getSabor()))
            return self.doritos
        elif opcao == 6 and self.coca_cola.getQtdEstoque() != 0:
            print('{nome} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.coca_cola.getNome()))
            return self.coca_cola
        elif opcao == 7 and self.sprite.getQtdEstoque() != 0:
            print('{nome} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.sprite.getNome()))
            return self.sprite
        elif opcao == 8 and self.guarana.getQtdEstoque() != 0:
            print('{nome} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.guarana.getNome()))
            return self.guarana
        elif opcao != 0:
            print('Produto indisponível no estoque!\n')
            return 9
        elif opcao == 0:
            return 0

    def verificarEntradaCompra(self):
        while True:
            try:
                resposta = int(input('É aceito somente notas de R$ 2,00 e R$ 5,00 ;)\nInsira a(s) nota(s) para o pagamento:\n'))
            except ValueError:
                print('ERRO, insira uma cédula válida!\n')
            else:
                while True:
                    try:
                        while resposta != 2 and resposta != 5:
                            resposta = int(input('É aceito somente notas de R$ 2,00 e R$ 5,00 ;)\nInsira a(s) nota(s) para o pagamento:\n0 - Cancelar\n'))
                    except ValueError:
                        print('ERRO, insira uma cédula válida!\n')
                    else:
                        return resposta

    def comprarProduto(self, produto, maquina):
        entrada_verificadora = maquina.verificarEntradaCompra()
        if produto.getValor() == 5:
            if entrada_verificadora == 2:
                if self.troco['qtdMoedasUmReal'] < 1:
                    print('No momento estamos impossibilitados de passar troco para essa compra.\n')
                else:
                    segunda_entrada = maquina.verificarEntradaCompra()
                    while segunda_entrada == 5:
                        print('Nessa compra é necessário SOMENTE cédulas de dois reais!\nInsira a segunda nota.\n')
                        segunda_entrada = maquina.verificarEntradaCompra()
                    terceira_entrada = maquina.verificarEntradaCompra()
                    while terceira_entrada == 5:
                        print('Nessa compra é necessário SOMENTE cédulas de dois reais!\nInsira a terceira nota.\n')
                        terceira_entrada = maquina.verificarEntradaCompra()
                    produto.decrementarEstoque()
                    self.receita_lucrativa += produto.getValor()
                    self.troco['qtdMoedasUmReal'] -= 1
                    print(produto.getQtdEstoque())
                    print('Valor repassado está correto!\nProduto e Troco prontos para retirada :)\nObrigado!\n################################\n')
            elif entrada_verificadora == 5:
                produto.decrementarEstoque()
                self.receita_lucrativa += produto.getValor()
                print(produto.getQtdEstoque())
                print('Valor repassado está correto!\nProduto pronto para retirada :)\nObrigado!\n################################\n')
        elif produto.getValor() == 4:
            if entrada_verificadora == 2:
                segunda_entrada = maquina.verificarEntradaCompra()
                while segunda_entrada == 5:
                    print('Nessa compra é necessário SOMENTE cédulas de dois reais!\nInsira a segunda nota.\n')
                    segunda_entrada = maquina.verificarEntradaCompra()
                produto.decrementarEstoque()
                self.receita_lucrativa += produto.getValor()
                print(produto.getQtdEstoque())
                print('Valor repassado está correto!\nProduto pronto para retirada :)\nObrigado!\n################################\n')
            elif entrada_verificadora == 5:
                if self.troco['qtdMoedasUmReal'] < 1:
                    print('No momento estamos impossibilitados de passar troco para essa compra.\n')
                else:
                    produto.decrementarEstoque()
                    self.receita_lucrativa += produto.getValor()
                    self.troco['qtdMoedasUmReal'] -= 1
                    print(produto.getQtdEstoque())
                    print('Valor repassado está correto!\nProduto e Troco prontos para retirada :)\nObrigado!\n################################\n')
        elif produto.getValor() == 2:
            if entrada_verificadora == 2:
                produto.decrementarEstoque()
                self.receita_lucrativa += produto.getValor()
                print(produto.getQtdEstoque())
                print('Valor repassado está correto!\nProduto pronto para retirada :)\nObrigado!\n################################\n')
            elif entrada_verificadora == 5:
                if self.troco['qtdMoedasUmReal'] < 3:
                    print('No momento estamos impossibilitados de passar troco para essa compra.\n')
                else:
                    produto.decrementarEstoque()
                    self.receita_lucrativa += produto.getValor()
                    self.troco['qtdMoedasUmReal'] -= 3
                    print(produto.getQtdEstoque())
                    print('Valor repassado está correto!\nProduto e Troco prontos para retirada :)\nObrigado!\n################################\n')