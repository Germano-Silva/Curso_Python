#estrutura de separação de argumentos dentro da função print.
print("argumento 1", "argumento 2")

#argumento não nomeado.
print(12, 34) 

#Argumento nomeado sep (separador) é utilizada para modigicar o modelo de separação que por inicial é espaço.
#pode ser utilizado tanto com aspas duplas como com aspas simples.
print(56, 78, sep="-")
print(9, 10, sep='*')

#Argumento nomeado end (final) é utilizado para adicionar algo ao final da função print.
#LF line fit - padonização de quebra de linha \n
print(1, 1, 2023, sep="-", end="\n")
#CRLF - padronização de quebra de linha \r\n
print(1, 1, 2023, sep="-", end="\r\n")

