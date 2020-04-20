from bebida import Bebida
from salgadinho import Salgadinho

#Ilustração da Máquina: 6 Seções com 4 divisorias cada, sendo que cada divisoria suporta 8 produtos
class Maquina(object):
    
    _resposta = 0

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
        self._receita_vendas = 0
        self.senha_administrativa = 'adm@7891'
    
    @property
    def receitaVendas(self):
        return self._receita_vendas

    def exibirInterfaceInicialUsuario(self):
        while True:
            try:
                print('Seja Bem-Vindo! Selecione umas das opções abaixo:')
                resposta = int(input('1 - Comprar Produto\n2 - Área Administrativa\n0 - Sair\n'))
            except ValueError:
                print('ERRO, informe somente números que correspondem as opções!\n')
            else:
                while True:
                    try:
                        while resposta < 0 and resposta > 2:
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
        if opcao == 1 and self.cheetos_cheddar.qtdEstoque != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_cheddar.nome,
            sabor = self.cheetos_cheddar.sabor))
            return self.cheetos_cheddar
        elif opcao == 2 and self.cheetos_parmesao.qtdEstoque != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_parmesao.nome,
            sabor = self.cheetos_parmesao.sabor))
            return self.cheetos_parmesao
        elif opcao == 3 and self.cheetos_queijo.qtdEstoque != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_queijo.nome,
            sabor = self.cheetos_queijo.sabor))
            return self.cheetos_queijo
        elif opcao == 4 and self.cheetos_requeijao.qtdEstoque != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.cheetos_requeijao.nome,
            sabor = self.cheetos_requeijao.sabor))
            return self.cheetos_requeijao
        elif opcao == 5 and self.doritos.qtdEstoque != 0:
            print('{nome} {sabor} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.doritos.nome,
            sabor = self.doritos.sabor))
            return self.doritos
        elif opcao == 6 and self.coca_cola.qtdEstoque != 0:
            print('{nome} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.coca_cola.nome))
            return self.coca_cola
        elif opcao == 7 and self.sprite.qtdEstoque != 0:
            print('{nome} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.sprite.nome))
            return self.sprite
        elif opcao == 8 and self.guarana.qtdEstoque != 0:
            print('{nome} em Estoque!\nVamos continuar com o processo de compra.\n'.format(nome = self.guarana.nome))
            return self.guarana
        elif opcao != 0:
            print('Produto indisponível no estoque!\n')
            return 9
        elif opcao == 0:
            return 0
    
    @staticmethod
    def verificarEntradaCompra():
        while True:
            try:
                _resposta = int(input('É aceito somente notas de R$ 2,00 e R$ 5,00 ;)\nInsira a(s) nota(s) para o pagamento:\n'))
            except ValueError:
                print('ERRO, insira uma cédula válida!\n')
            else:
                while True:
                    try:
                        while _resposta != 2 and _resposta != 5:
                            _resposta = int(input('É aceito somente notas de R$ 2,00 e R$ 5,00 ;)\nInsira a(s) nota(s) para o pagamento:\n'))
                    except ValueError:
                        print('ERRO, insira uma cédula válida!\n')
                    else:
                        return _resposta

    def comprarProduto(self, produto):
        entrada_verificadora = Maquina.verificarEntradaCompra()
        if produto.valor == 5:
            if entrada_verificadora == 2:
                if self.troco['qtdMoedasUmReal'] < 1:
                    print('No momento estamos impossibilitados de passar troco para essa compra.\n')
                else:
                    segunda_entrada = Maquina.verificarEntradaCompra()
                    while segunda_entrada == 5:
                        print('Nessa compra é necessário SOMENTE cédulas de dois reais!\nInsira a segunda nota.\n')
                        segunda_entrada = Maquina.verificarEntradaCompra()
                    terceira_entrada = Maquina.verificarEntradaCompra()
                    while terceira_entrada == 5:
                        print('Nessa compra é necessário SOMENTE cédulas de dois reais!\nInsira a terceira nota.\n')
                        terceira_entrada = Maquina.verificarEntradaCompra()
                    produto.decrementarEstoque()
                    self._receita_vendas += produto.valor
                    self.troco['qtdMoedasUmReal'] -= 1
                    print('Valor repassado está correto!\n{nome} e Troco(R$ {troco}.00) prontos para retirada :)\nObrigado!\n################################\n'.format(nome = produto.nome, troco = 1))
            elif entrada_verificadora == 5:
                produto.decrementarEstoque()
                self._receita_vendas += produto.valor
                print('Valor repassado está correto!\n{nome} pronto para retirada :)\nObrigado!\n################################\n'.format(nome = produto.nome))
        elif produto.valor == 4:
            if entrada_verificadora == 2:
                segunda_entrada = Maquina.verificarEntradaCompra()
                while segunda_entrada == 5:
                    print('Nessa compra é necessário SOMENTE cédulas de dois reais!\nInsira a segunda nota.\n')
                    segunda_entrada = Maquina.verificarEntradaCompra()
                produto.decrementarEstoque()
                self._receita_vendas += produto.valor
                print('Valor repassado está correto!\n{nome} pronto para retirada :)\nObrigado!\n################################\n'.format(nome = produto.nome))
            elif entrada_verificadora == 5:
                if self.troco['qtdMoedasUmReal'] < 1:
                    print('No momento estamos impossibilitados de passar troco para essa compra.\n')
                else:
                    produto.decrementarEstoque()
                    self._receita_vendas += produto.valor
                    self.troco['qtdMoedasUmReal'] -= 1
                    print('Valor repassado está correto!\n{nome} e Troco(R$ {troco}.00) prontos para retirada :)\nObrigado!\n################################\n'.format(nome = produto.nome, troco = 1))
        elif produto.valor == 2:
            if entrada_verificadora == 2:
                produto.decrementarEstoque()
                self._receita_vendas += produto.valor
                print('Valor repassado está correto!\n{nome} pronto para retirada :)\nObrigado!\n################################\n'.format(nome = produto.nome))
            elif entrada_verificadora == 5:
                if self.troco['qtdMoedasUmReal'] < 3:
                    print('No momento estamos impossibilitados de passar troco para essa compra.\n')
                else:
                    produto.decrementarEstoque()
                    self._receita_vendas += produto.valor
                    self.troco['qtdMoedasUmReal'] -= 3
                    print('Valor repassado está correto!\n{nome} e Troco(R$ {troco}.00) prontos para retirada :)\nObrigado!\n################################\n'.format(nome = produto.nome, troco = 3))
    
    def vericarSenhaAdministrativa(self):
        senha = input('Informe a senha administrativa:\n')
        while senha != self.senha_administrativa:
            senha = input('Senha INCORRETA!\nInforme a senha administrativa:\n')

    def listarFuncionalidadesAdministrativas(self):
        while True:
            try:
                print('Seja Bem-Vindo! Selecione umas das opções abaixo:')
                resposta = int(input('1 - Exibir Valor de Vendas\n0 - Sair\n'))
            except ValueError:
                print('ERRO, informe somente números que correspondem as opções!\n')
            else:
                while True:
                    try:
                        while resposta != 0 and resposta != 1:
                            print('Número digitado INCORRETO, tente mais uma vez!\n')
                            resposta = int(input('1 - Exibir Valor de Vendas\n0 - Sair\n'))
                    except ValueError:
                        print('ERRO, informe somente os números que correspondem as opções!\n')
                    else:
                        return resposta