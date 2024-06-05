# Tipo tupla - Uma lista imutável
# A tupla funciona como uma lista.
# porem  mesma é imutavel utilizando os metodos do obj
# As tuplas são mais rapidas que a lista

nomes = 'Maria', 'Helena', 'Luiz'
_, nome1, *resto = nomes
print(nomes)
print(nome1)

# fazendo conversão de lista mutavel para tuple (LISTA IMUTVEL)
lista = ['Maria', 'Helena', 'Luiz']
lista = tuple(lista)
print(lista)
print(lista[-1])

#Convertendo para uma lista mutavel
lista = list(lista)
print(lista)