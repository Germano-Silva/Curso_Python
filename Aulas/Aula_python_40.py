""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

# Este bloco de código está tentando converter as strings de entrada `numero_1` e `numero_2` em
# números de ponto flutuante usando a função `float()`. Se a conversão for bem sucedida sem qualquer
# erros, ele define a variável `numeros_validos` como `True`, indicando que os números de entrada são
# válido e pode ser usado para cálculos adicionais.
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

# Este bloco de código está verificando se a variável `numeros_validos` é `None`. Se for `Nenhum`, será
# significa que um ou ambos os números inseridos pelo usuário são inválidos (não podem ser convertidos para
# Números de ponto flutuante). Neste caso, imprime uma mensagem informando ao usuário que os números estão
# inválido e então usa a instrução `continue` para pular o resto da iteração atual do
# `while` faz um loop e passa para a próxima iteração, solicitando que o usuário insira números novamente.
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

# Esta parte do código está realizando a validação de entrada para o operador inserido pelo usuário. Aqui está
# o que cada parte faz:
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

# Esta parte do código executa operações aritméticas com base na entrada do operador pelo usuário.
# Aqui está o que cada parte faz:
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

# Este bloco de código pergunta ao usuário se ele deseja sair da calculadora.
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break