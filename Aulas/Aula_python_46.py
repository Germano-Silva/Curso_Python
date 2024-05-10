# Este trecho de código Python está usando uma estrutura de loop aninhado com uma combinação de `for` e `if`
# declarações. Aqui está um resumo do que ele faz:
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')