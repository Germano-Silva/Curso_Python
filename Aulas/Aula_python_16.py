# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')
# validando a entrada em bloco dondicional.
if entrada == 'entrar':
    print('Você entrou no sistema')
# verificado bloco
    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')
# validando que fora do bloco mesmo sendo em baixo da condição o codigo vai ser executado
# pois não faz parte da condição ou do boco dondicional.
print('FORA DOS BLOCOS')