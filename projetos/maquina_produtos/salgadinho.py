from produto import Produto

class Salgadinho(Produto):

    def __init__(self, nome, sabor, valor, qtd_estoque, peso):
        super().__init__(nome, sabor, valor, qtd_estoque)
        self._peso = peso

    @property
    def peso(self):
        return self._peso
    
    def __str__(self):
        return '{nome} {sabor} {peso} : R$ {valor},00'.format(nome = self._nome, sabor = self._sabor, 
        peso = self._peso, valor = self._valor)