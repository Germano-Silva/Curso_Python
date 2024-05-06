nome = 'Germano'
altura = 1.72
peso = 85
imc = peso/(altura**2)


#  deve sair em formato
# luis otavio tem 1,80 de altura, 
# pesa 95 quilos e seu IMC é 
# 29,3209876543202987
ellipsis = ...#place roder codigo que ao executar não gera erro.

# f-strings  f = format = formatação
linha_01 = f'{nome} tem {altura:.2f} de altura,'
linha_02 = f'pesa {peso} quilos e seu IMC é '
linha_03 = f'{imc:.2f}'

print(linha_01)
print(linha_02)
print(linha_03)
