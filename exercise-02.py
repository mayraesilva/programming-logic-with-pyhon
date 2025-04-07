# Faça um Programa para uma loja de tintas.

# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas 
# e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima,
#     isto é, considere latas cheias.

import math

area = float(input('Insira a área que deseja pintar em m²: '))

def cobertura_tintas(area):
    #1m² precisa de 6 litros
    quantidade_em_litros = area / 6
    #Apenas latas
    quantidade_latas = math.ceil(quantidade_em_litros / 18) #quantidade de latas arredontada para a maior
    valor_latas = quantidade_latas * 80
    print(f'Se deseja comprar apenas latas, deve comprar {quantidade_latas} latas, valor total R${valor_latas},00')
    
    #Apenas galões
    quantidade_galoes = math.ceil(quantidade_em_litros /3.6) #quantidade de galões necessária
    valor_galoes = quantidade_galoes * 25
    print(f'Se deseja comprar apenas galoes, deve comprar {quantidade_galoes} galoes, valor total R${valor_galoes},00')

    #Misturando latas e galões
    quantidade_parcial_latas =  int(quantidade_em_litros / 18)
    quantidade_parcial_galoes = int(quantidade_em_litros / 3.6)
    
    #completanto a área
    resto_lata = quantidade_em_litros % 18
    complemento_quantidade_galao = math.ceil((math.ceil(resto_lata)) / 3.6) 

    resto_galao = quantidade_em_litros % 3.6
    complemento_quantidade_lata = math.ceil((math.ceil(resto_galao)) / 18)


    valor_maioria_lata = quantidade_parcial_latas * 80 + complemento_quantidade_galao * 25
    valor_maioria_galao = quantidade_parcial_galoes * 25 + complemento_quantidade_lata * 80

    if valor_maioria_lata > valor_maioria_galao:
        return f'Você deve comprar {quantidade_parcial_latas} latas e {complemento_quantidade_galao} galoes, total R${valor_maioria_lata},00'
    
    elif valor_maioria_galao > valor_maioria_lata:
        return f'Você deve comprar {quantidade_parcial_galoes} galões e {complemento_quantidade_lata} lata, total R${valor_maioria_galao},00'
    
    

print(cobertura_tintas(area))






