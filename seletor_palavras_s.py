st = 'Print only the words that start with s in this sentence'
palavras = st.split()
lista_palavras_s = []
for palavra in palavras:
    if (palavra[0].lower() == 's'):
        lista_palavras_s.append(palavra)
print(lista_palavras_s)