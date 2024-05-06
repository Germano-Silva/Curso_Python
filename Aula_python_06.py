# Conversção de tipos, coerção
# Type convertion, typecasting, coercion
#é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1+1) # Tipagem dinamica
print('a'+'b') # concatenação 
print('1'+1) # concatenação somente em str com str e não com str e int
print(int('1'), type(int('1'))) #coerção de tipo 
# Desta maneira vai fazer com que o tipo seja trocado.
print(int('1') + 1) #dessa maneira vai ser possivel realizar a soma de dois número inteiros porem antes tem que realizar a troca do tipo.
#quando houver qualquer tipo de operação com um tipo float o resultado vai ser do tipo float
#str com float erro, str não realiza operações.
print(float('1') + 1)
# em bool é considerado falso quando a str é vazia
print(bool(''))
# em bool é considerado True quando a str não for vazia
print(bool(' '))
# A coersão pode ser feita para qualque tipo so tem que seguir um padrão como tipo(Vareavel)
print(int('1'))
print(float('1'))
print(str(1))
print(bool('1'))