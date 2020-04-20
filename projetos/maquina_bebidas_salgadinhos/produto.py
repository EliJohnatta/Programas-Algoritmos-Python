class Produto(object):
    
    def __init__(self, nome, sabor, valor, qtd_estoque):
        self._nome = nome
        self._sabor = sabor
        self._valor = valor
        self._qtd_estoque = qtd_estoque

    @property
    def nome(self):
        return self._nome

    @property
    def sabor(self):
        return self._sabor

    @property
    def valor(self):
        return self._valor
    
    @property
    def qtdEstoque(self):
        return self._qtd_estoque
    
    def decrementarEstoque(self):
        self._qtd_estoque -= 1 