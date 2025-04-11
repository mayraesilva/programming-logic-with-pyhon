#Uma nova tentativa

# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores
# para saber qual o melhor jogador após cada jogo. 
# Para isto, faz-se necessário o desenvolvimento de um programa, 
# que será utilizado pelas telefonistas, para a computação dos votos.
# Sua equipe foi contratada para desenvolver este programa. 
# Para computar cada voto, a telefonista digitará um número, entre 1 e 23, 
# correspondente ao número da camisa do jogador.
# Um número de jogador igual zero, indica que a votação foi encerrada. 
# Se um número inválido for digitado, o programa deve ignorá-lo, 
# mostrando uma breve mensagem de aviso, 
# e voltando a pedir outro número. 
# Após o final da votação, o programa deverá exibir: 
# O total de votos computados; 
# Os númeos e respectivos votos de todos os jogadores que receberam votos; 
# O percentual de votos de cada um destes jogadores; 
# O número do jogador escolhido como o melhor jogador da partida, 
# juntamente com o número de votos e o percentual de votos dados a ele. 
# Observe que os votos inválidos e o zero final não devem ser computados como votos. 
# O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. 
# O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
# Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
# A função calculará o percentual e retornará o valor calculado.

# Exemplo: Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9 
# Número do jogador (0=fim): 10 
# Número do jogador (0=fim): 9 
# Número do jogador (0=fim): 10 
# Número do jogador (0=fim): 11 
# Número do jogador (0=fim): 10 
# Número do jogador (0=fim): 50 

# Informe um valor entre 1 e 23 ou 0 para sair! 
# Número do jogador (0=fim): 9 
# Número do jogador (0=fim): 9 
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.

# Jogador Votos % 
# 9 4 50,0% 
# 10 3 37,5% 
# 11 1 12,5% 
# O melhor jogador foi o número 9,
# com 4 votos, correspondendo a 50% do total de votos.


def best_player():

    votos = [] #votos armazenados 
    jogador = 0
    total_votos_por_jogador = {}

    while jogador != '0': #até 0 ser acionado
        jogador = input('Informe um valor entre 1 e 23: ')
        
        if int(jogador) in range(1, 24):
            votos.append(jogador)


        else: #caso não seja encontrado o jogador

            while int(jogador) not in range (0, 24):
                jogador = input(f'O jogador número {jogador} não foi identificado, insira um número válido: ')

                if int(jogador) in range(0,24): #só acrescenta quando estiver no grupo
                    votos.append(jogador)
    
    #print(votos)
    total_votos = len(votos)

    #adiciconando jogadores ao dict
    for jogador in votos: #Iniciando o dicionário com jogadores que receberam votos
        total_votos_por_jogador.update({jogador : 0})

  
    print(total_votos_por_jogador)

    #Iniciando a contagem de votos
    for voto in votos:
        total_votos_por_jogador[voto] += 1
    
    #print(total_votos_por_jogador)

    
    mais_votados = sorted(total_votos_por_jogador.items(), key=lambda item: item[1], reverse=True)

    #print(mais_votados)
    
    

    #Resultados
    print(f'O jogador mais votado foi o  jogador {mais_votados[0][0]}, com {mais_votados[0][1]} votos e {((mais_votados[0][1] / total_votos)*100):.1f}% dos votos totais' )
    if len(mais_votados) > 1:
        print(f'O segundo jogador mais votado foi o jogador {mais_votados[1][0]}, com {mais_votados[1][1]} votos e {((mais_votados[1][1] / total_votos)*100):.1f}% dos votos totais' )
    
    if len(mais_votados) > 2:
        print(f'O terceiro jogador mais votado foi o jogador {mais_votados[2][0]}, com {mais_votados[2][1]} votos e {((mais_votados[2][1] / total_votos)*100):.1f}% dos votos totais' )
        
    print(f'Lembrando que nessa votação tivemos {total_votos} votos') 


    return


best_player()