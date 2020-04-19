class Produto(object):
    
    def __init__(self, nome, sabor, valor, qtd_estoque):
        self.nome = nome
        self.sabor = sabor
        self.valor = valor
        self.qtd_estoque = qtd_estoque

    def getNome(self):
        return self.nome

    def getSabor(self):
        return self.sabor

    def getValor(self):
        return self.valor
    
    def getQtdEstoque(self):
        return self.qtd_estoque
    
    def decrementarEstoque(self):
        self.qtd_estoque -= 1 