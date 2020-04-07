try:
    for i in ['a', 'b', 'c', 'd']:
        print(i**2)
except TypeError:
    print('Erro ao tentar realizar operação matemática com strings')
else:
    print('Execução bem sucessida')
finally:
    print('Fim de código')