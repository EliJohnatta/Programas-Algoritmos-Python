from produto import Produto

class Bebida(Produto):

    def __init__(self, nome, sabor, valor, qtd_estoque, volume):
        #Produto.__init__(self, nome, sabor, valor, qtd_estoque)
        super().__init__(nome, sabor, valor, qtd_estoque)
        self._volume = volume
    
    @property
    def volume(self):
        return self._volume
    
    def __str__(self):
        return '{nome} {sabor} {volume} : R$ {valor},00'.format(nome = self._nome, sabor = self._sabor, 
        volume = self._volume, valor = self._valor)
    
    
    