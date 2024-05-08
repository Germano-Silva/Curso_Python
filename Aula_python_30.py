"""
CONSTANTE ="Variaveis" que não vão mudar
muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro =90 #local em que o carro está na estrada.

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 esta
RADAR_RANGE = 1 # A distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')
if local_carro >= (LOCAL_1-RADAR_RANGE) and\
    local_carro<=(LOCAL_1+RADAR_RANGE) and \
        velocidade>RADAR_1:
    print('Carro multado em radar 1')

# Melhorando o codigo

velocidade_2 = 61 #velocidade atual do carro
local_carro_2 =90 #local em que o carro está na estrada.

RADAR_2 = 60 # Velocidade máxima do radar 1
LOCAL_2 = 100 # Local onde o radar 1 esta
RADAR_RANGE_2 = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade_2>RADAR_2
carro_passou_radar_1 = local_carro_2 >= (LOCAL_2-RADAR_RANGE_2) and local_carro_2<=(LOCAL_2+RADAR_RANGE_2)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')
if carro_passou_radar_1:
    print('Carro passou radar 1')
if carro_multado_radar_1:
    print('Carro multado em radar 1')