raio = int(input('Informe o raio: '))

def volume_esfera(r):
    return (4/3) * 3.14 * (r ** 3)

print('Volume: %1.2f' %volume_esfera(raio))