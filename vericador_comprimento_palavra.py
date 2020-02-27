st = 'Print every word in this sentence that has an even number of letters '
palavras = st.split()
for palavra in palavras:
    tamanho = len(palavra)
    if tamanho % 2 == 0:
        print('{} --- tem comprimento par'.format(palavra))
    else:
        print('{} --- tem comprimento impar'.format(palavra))