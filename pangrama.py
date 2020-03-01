import string

frase1 = 'The quick brown fox jumps over the lazy dog'
frase2 = 'The quick brown fox jumps over the lay dog'

def pangrama(str , alfabeto = string.ascii_lowercase):
    set_str = set(str.lower())
    set_alfabeto = set(alfabeto)
    set_str.remove(' ')
    return set_str == set_alfabeto

print(pangrama(frase1))
print(pangrama(frase2))

