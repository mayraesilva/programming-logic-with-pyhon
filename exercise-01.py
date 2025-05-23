#Exercício 01

# João Papo-de-Pescador, homem de bem, comprou um microcomputador 
# para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar 
# uma multa de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que 
# leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável 
# multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

peso_de_peixes = float(input('Insira a quantidade pescada'))

def regulamento_pesca_sp(peso_de_peixes): 
    if peso_de_peixes > 50:
        excesso = peso_de_peixes - 50
        multa = excesso * 4
        return f'O peso em kg da pesca é {peso_de_peixes}, \n esse valor excede em {excesso} kg, \n deve pagar multa de {multa} reais'

    else:
        return f'O peso em kg da pesca é {peso_de_peixes}, portanto não excede o valor máximo'
        
print(regulamento_pesca_sp(peso_de_peixes))