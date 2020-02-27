numeros = list(range(0,11,1))
numeros_pares = []
for item in numeros:
    if item % 2 == 0:
        numeros_pares.append(item)
print(numeros_pares)