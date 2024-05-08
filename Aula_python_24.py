# Operadores in e not in
# Strings são iteráveis - navegação item por item  inicindo do indice 
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Germano'
print(nome[2])
print(nome[-4])
print('á' in nome)
print('m' in nome)
print(10 * '-')
print('mano' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')