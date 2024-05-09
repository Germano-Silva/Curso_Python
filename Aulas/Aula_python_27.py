"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
# Fatiamento de indice por indice
print(variavel[4]) #adiciona-se somente o indice que deseja

# Fatiamento por pedassos 
# Fatiamento [inicio:fim:pedaço] [::]
print(variavel[4:])
# a partir do indice 4 ao final 
# lembrando que o final não é incluido.

# Fatiamento com informação de até onde deve ir 
print(variavel[0:5])

# Fatiamento por passo
# O fatiamento por passo e a amotrsgem de acordo com a quantidade de passos solicitados
# No passo abaixo mostra que a a fraze vai mostrar de 2 em 2 caracteres do inicio ao fim da fraze
print(variavel[0:9:2])

# Utilizando a metodo len para contagem de str
# utilizando len a contagem sempre começa do 1 
print(len(variavel))

# Utilizando o metodo com len com o modelo de fatiamento
print(variavel[0:len(variavel):2])

# invertendo a string
print(variavel[-1:-10:-1])