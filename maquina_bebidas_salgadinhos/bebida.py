from produto import Produto

class Bebida(Produto):

    def __init__(self, nome, sabor, valor, qtd_estoque, volume):
        #Produto.__init__(self, nome, sabor, valor)
        super().__init__(nome, sabor, valor, qtd_estoque)
        self.volume = volume
    
    def getVolume(self):
        return self.volume
    
    def __str__(self):
        return '{nome} {sabor} {volume} : R$ {valor},00'.format(nome = self.nome, sabor = self.sabor, 
        volume = self.volume, valor = self.valor)
    
    
    