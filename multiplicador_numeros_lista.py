lista_numeros = [1, 2, 3, -4, -5]

def multiplicar_numeros_lista(lista):
    produto = 1
    for numero in lista:
        produto *= numero
    return produto

print(multiplicar_numeros_lista(lista_numeros))