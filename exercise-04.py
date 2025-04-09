

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


def vote_count(votes): #recebe a lista contendo votos

    #Possibilidades de votos:
    jogador_01 = []
    jogador_02 = []
    jogador_03 = []
    jogador_04 = []
    jogador_05 = []
    jogador_06 = []
    jogador_07 = []
    jogador_08 = []
    jogador_09 = []
    jogador_10 = []
    jogador_11 = []
    jogador_12 = []
    jogador_13 = []
    jogador_14 = []
    jogador_15 = []
    jogador_16 = []
    jogador_17 = []
    jogador_18 = []
    jogador_19 = []
    jogador_20 = []
    jogador_21 = []
    jogador_22 = []
    jogador_23 = []

    for vote in votes:

        if vote == '1':
            jogador_01.append(vote)
        
        elif vote == '2':
            jogador_02.append(vote)

        elif vote == '3':
            jogador_03.append(vote)

        elif vote == '4':
            jogador_04.append(vote)

        elif vote == '5':
            jogador_05.append(vote)

        elif vote == '6':
            jogador_06.append(vote)

        elif vote == '7':
            jogador_07.append(vote)

        elif vote == '8':
            jogador_08.append(vote)

        elif vote == '9':
            jogador_09.append(vote)

        elif vote == '10':
            jogador_10.append(vote)

        elif vote == '11':
            jogador_11.append(vote)

        elif vote == '12':
            jogador_12.append(vote)

        elif vote == '13':
            jogador_13.append(vote)

        elif vote == '14':
            jogador_14.append(vote)

        elif vote == '15':
            jogador_15.append(vote)

        elif vote == '16':
            jogador_16.append(vote)
        
        elif vote == '17':
            jogador_17.append(vote)

        elif vote == '18':
            jogador_18.append(vote)

        elif vote == '19':
            jogador_19.append(vote)

        elif vote == '20':
            jogador_20.append(vote)

        elif vote == '21':
            jogador_21.append(vote)

        elif vote == '22':
            jogador_22.append(vote)

        elif vote == '23':
            jogador_23.append(vote)
        
        elif vote == '0':
            break

    
    total_de_votos_por_jogador = {
    "Jogador 1": len(jogador_01),
    "Jogador 2": len(jogador_02),
    "Jogador 3": len(jogador_03),
    "Jogador 4": len(jogador_04),
    "Jogador 5": len(jogador_05),
    "Jogador 6": len(jogador_06),
    "Jogador 7": len(jogador_07),
    "Jogador 8": len(jogador_08),
    "Jogador 9": len(jogador_09),
    "Jogador 10": len(jogador_10),
    "Jogador 11": len(jogador_11),
    "Jogador 12": len(jogador_12),
    "Jogador 13": len(jogador_13),
    "Jogador 14": len(jogador_14),
    "Jogador 15": len(jogador_15),
    "Jogador 16": len(jogador_16),
    "Jogador 17": len(jogador_17),
    "Jogador 18": len(jogador_18),
    "Jogador 19": len(jogador_19),
    "Jogador 20": len(jogador_20),
    "Jogador 21": len(jogador_21),
    "Jogador 22": len(jogador_22),
    "Jogador 23": len(jogador_23)
    }

    mais_votados = sorted(total_de_votos_por_jogador.values(), reverse=True)
    print(mais_votados)

    pass

    






def best_player(total_de_votos=8):

    votos = []

    while total_de_votos != 0: #até não ter mais quem votar
        total_de_votos = total_de_votos - 1
        jogador = input('Informe um valor entre 1 e 23: ')

        if int(jogador) in range(0,24):
            votos.append(jogador)

        else: #caso não seja encontrado o jogador

            while int(jogador) not in range (0,24):
                jogador = input(f'O jogador número {jogador} não foi identificado, insira um número válido: ')

                if int(jogador) in range(0,24): #só acrescenta quando estiver no grupo
                    votos.append(jogador)
    
    print(votos)
    
    mais_votados = vote_count(votos)



    print(mais_votados)
    
    #return(votos)



    pass


best_player()
