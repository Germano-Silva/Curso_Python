"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

# O código `for letra in texto: print(letra)` está iterando sobre cada caractere da variável string
# `texto` e imprimindo cada caracter um por um. Isso é possível porque strings em Python são
# objetos iteráveis, o que significa que você pode fazer um loop sobre eles caractere por caractere usando um loop `for`.
for letra in texto:
    print(letra)