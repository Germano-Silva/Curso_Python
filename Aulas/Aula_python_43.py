# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
# Este código está iterando sobre cada caractere da string `texto`, que é 'Python'. Para cada
# caractere, é adicionar um asterisco (*) antes do caractere e anexá-lo ao `novo_texto`
# variável.
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')