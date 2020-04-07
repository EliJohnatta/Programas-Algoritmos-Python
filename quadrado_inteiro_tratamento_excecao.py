def quadrado_numero():
    flag = True
    while flag:
        try:
            i = int(input('Inteiro ---> '))
            q = i*2
        except ValueError:
            print('Erro, informe um número inteiro')
        else:
            print('Resultado: {q}'.format(q = q))
            flag = False

quadrado_numero()