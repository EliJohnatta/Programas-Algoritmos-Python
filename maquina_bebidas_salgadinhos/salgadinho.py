from produto import Produto

class Salgadinho(Produto):

    def __init__(self, nome, sabor, valor, qtd_estoque, peso):
        super().__init__(nome, sabor, valor, qtd_estoque)
        self.peso = peso

    def getPeso(self):
        return self.peso
    
    def __str__(self):
        return '{nome} {sabor} {peso} : R$ {valor},00'.format(nome = self.nome, sabor = self.sabor, 
        peso = self.peso, valor = self.valor)