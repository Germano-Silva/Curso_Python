"""
For + Range
range -> range(start, stop, step)
"""
# Este trecho de código está criando um intervalo de números começando de 0 até (mas não incluindo) 100 com
# um tamanho de passo de 8. A chamada de função `range(0, 100, 8)` gera números em incrementos de 8 dentro
# o intervalo especificado.
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)