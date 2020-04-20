st = 'Create a list of the first letters of every word in this string'
lista_palavras = st.split()
#Compreensão em Listas
lista_letras_iniciais = [palavra[0] for palavra in lista_palavras]
print(lista_letras_iniciais)