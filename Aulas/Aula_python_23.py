# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha == '123456':
    print('entrou!')
else:
    print('senha incorreta.')

if senha != '123456':
    print('senha incorreta.')

if not senha:
    print('senha incorreta.')


print(not True)  # False
print(not False)  # True