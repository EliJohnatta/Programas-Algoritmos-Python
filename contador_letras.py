str = 'Olá Sr. Rogers, como você está bem, terça-feira?'



def contador_letras(str):
    #Utilizando Dicionário
    d = {'maiusculas' : 0, 'minusculas' : 0, 'outros' : 0}
    for letra in str:
        if letra.isupper():
            d['maiusculas'] += 1
        elif letra.islower():
            d['minusculas'] += 1
        else:
            d['outros'] += 1
    print('Maiúsculas: {a}, Minúsculas {b}, Outros Caracteres: {c}'.format(a = d['maiusculas'], b = d['minusculas'], c = d['outros']))
contador_letras(str)
