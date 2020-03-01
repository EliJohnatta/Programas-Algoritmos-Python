lista_numeros_repetidos = [1,1,2,2,3,4,5,6,1,1]

def transformador(lista):
    lista_numeros_exclusivos = set(lista)
    return list(lista_numeros_exclusivos)

print (transformador(lista_numeros_repetidos))