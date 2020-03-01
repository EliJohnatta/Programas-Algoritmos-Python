numero, int_inicio, int_final = input().split()
numero = int(numero)
int_inicio = int(int_inicio)
int_final = int(int_final)

def intervalo_numeros(n, inicio, final):
    return inicio <= n <= final

print(intervalo_numeros(numero, int_inicio, int_final))