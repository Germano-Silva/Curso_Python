"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Vou dobrar o número que você digitar:')
numero_float = float(numero)
print(f'Odobro de {numero} é {numer_float * 2:.2f}')

numero_str = input('Vou dobrar o número que você digitar:')
try:
    print('str:', numero_str)
    numer_float2 = float(numero_str)
    print('Float: ' numero_float)
    print(f'O dobro de {numero_str} é {numer_float*2:.2f}')

except:
    print('Isso não é um número.')