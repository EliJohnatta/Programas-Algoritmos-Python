class Cilindro(object):

    pi = 3.14

    def __init__(self,raio,altura):
        self.raio = raio
        self.altura = altura
    
    def getAreaLateral(self):
        return 2*Cilindro.pi*self.raio*self.altura

    def getAreaBase(self):
        return Cilindro.pi*(self.raio**2)

    def getAreaTotal(self):
        return 2*Cilindro.pi*self.raio*(self.altura+self.raio)

    def getVolume(self):
        return Cilindro.pi*(self.raio**2)*self.altura

c1 = Cilindro(2,4)
at = c1.getAreaTotal()
v = c1.getVolume()
print('Área Total: {a}\nVolume: {v}'.format(a = at, v = v))