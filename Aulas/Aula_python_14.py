a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
# Parametro nomeado - nomeando o argumento e atribuindo a uma vareavel
# Qunado usamos um paramentro nomeado tudo que vir depois dele deve ser nomeado
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

# Tudo em Python é objeto e todo objeto em Python tem metodos que poder ser utilizado
# 
d = 'C'
e = 'D'
f = 2.1
string = 'C={} D={} E={:.2f}'
# argumento 
formato = string.format(d, e, f)

print(formato)


# Indices OBS: todo indice inicia-se do 0
k = 'K'
l = 'L'
m = 4.1
# Para formatar de maneira a seguir um padrão usamos o indece do argumento correspondente
string = 'K={0} L={1} M={2:.2f}'
# argumento 
formato = string.format(k, l, m)
print(formato)
# Pode-se usar o indice para alterar a ordem ou duplicar o argumento.
string = 'K={0} K={1} L={1} N={2} M={2:.2f}'
# argumento 
formato = string.format(k, l, m)
print(formato)

g = 'G'
h = 'H'
i = 3.1
string = 'G={} H={} I={:.2f} J={}'
# argumento 
formato = string.format(g, h, i)
# vai apresentar erro porque tem mais argumentos que a função
print(formato)