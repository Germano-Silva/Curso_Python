"""
Introdução ao empacotamento e desempacotamento
"""

#para o desempacotamento dar certo é preciso ter a mesma quantidade de valores para variaveis.
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome1, nome2, nome3)

# Caso querira realizar o desenpacotamente de um valor 
# e depois empacotar o resto dos valores em uma varivel
# adiciona-se o "*" antes da variavel
nome4, *resto = ['Maria', 'Helena', 'Luiz']
print(nome4, resto)

#Quando não se deseja utilizar uma variavel utiliza-se a convenção Python
#Subistitui a variavel pelo "_"
nome5, *_ = ['Maria', 'Helena', 'Luiz']
print(nome5, _)

# Subistituir a variavel pelo "_" para pular valores
_, _, nome6 = ['Maria', 'Helena', 'Luiz']
print(_, nome6)

# Caso não tenha a mesma quantidade de valores que variaveis ira apresentar o erro:
# ValueError: not enough values to unpack (expected 4, got 3)
erro2, erro3, erro4, erro5 = ['Maria', 'Helena', 'Luiz']
print(erro2, erro3, erro4, erro5)

# Caso não tenha a mesma quantidade de variaveis que valor ira apresentar o erro:
# ValueError: too many values to unpack (expected 1)
erro1, = ['Maria', 'Helena', 'Luiz']
print(erro1)





