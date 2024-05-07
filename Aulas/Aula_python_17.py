# if / elif      / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

# Se as condissoes tiverem o mesmo resultado a primeira que for executada vai impedir que as outras sejam executadas pelo imterpretador 
# fazendo com que a condição execute o primeiro resultado correspondente e saindo do bloco de condição.

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    # pass pode ser utilizado como a ... para utilizar em locais que você quer que tenha um codigo no futuro.
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')