"""
enumerate - enumera iteráveis (índices)
Ele enúmera cada item da sua lista adicionado o indice 
Transformando em matriz de dois itens 
Transformando em tuplas não mutaveis 
podendo escolher de onde começa os indices da tupla criada 
"""

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']

print("possui varias maneiras de visualisar a tupla criada")
print("\n\n")
print("nesta primeira vai apresentar o obj de memoria do iterator")
lista_enumerada = enumerate(lista)
print(lista_enumerada)
print("\n\n")

print("nesta 2ª vai apresentar a primeira tupla")
lista_enumerada = enumerate(lista)
print(next(lista_enumerada))
print("\n\n")

print("nesta 3ª opção vai sair um por vez devido usar o for")
for item in lista_enumerada:
    print(item)
print("\n\n")
print("Depois da utilçização do enumarete dessa maneura não é possivel utilizar novamente pois o python")
print("intende que a tupla foi consumida e deve ser eliminada não contendo mais obj para serem utilizados")


print("nesta 4ª opção vai sair um por vez devido usar o for e o enumarate direto na função")
print("fazendo com que não se perca as informações para serem utilizadas")
lista2 = ['Maria', 'Helena', 'Luiz']
for item2 in  enumerate(lista2):
    print(item2)
print("\n\n")

print("nesta 5ª opção vai sair um por vez devido usar o for ")
print("e o enumarate direto na função e modificação de tipo")
print("fazendo com que não se perca as informações para serem utilizadas")
for item2 in  list(enumerate(lista2)):
    print(item2)
print("\n\n")

print("Jeito correto para que não perca os itens")
print("e que mantenha a formatação de visualização")
print("como se fosse uma stringue na saida ")
print("Separando os items em objetos ")
for indice, nome in list(enumerate(lista2)):
    print(indice, nome)
print("\n\n")

print("como funciona internamente o for com separadores")
for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
print("\n\n")

print("Mostrando a lista com o nome a lista e o indice")
lista3 = ['Maria', 'Helena', 'Luiz', 'João']

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
print("\n\n")


