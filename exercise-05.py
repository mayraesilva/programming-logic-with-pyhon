#Tentativa 1 de Mayra Silva

# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete
#  feita a um grande quantidade de organizações: 
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:
# 1- Windows Server 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete
#  e informe ao final o resultado da mesma. 
# O programa deverá ler os valores até ser informado o valor 0, 
# que encerra a entrada dos dados. 
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
#  Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
# Após os dados terem sido completamente informados, 
# o programa deverá calcular a percentual de cada um dos concorrentes 
# e informar o vencedor da enquete. 
# O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional Votos %

# Windows Server 1500 17% Unix 3500 40% Linux 3000 34% Netware 500 5% Mac OS 150 2% Outro 150 2%

# Total 8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.





def best_OS():
    operational_systems = {'Windows Server' : 1, 'Unix' : 2, 'Linux' : 3, 
                           'Netware' : 4, 'Mac OS' : 5, 'Outro' : 6  }
    
    #contadores de votos para cada sistema operacional
    windows_server_votes = 0
    unix_votes = 0
    linux_votes = 0
    netware_votes = 0
    mac_os_votes = 0
    outro_votes = 0



    #Votos
    votos_sistema = [windows_server_votes, unix_votes, linux_votes,
                      netware_votes, mac_os_votes, outro_votes]
    voto = 0


    while voto != '0':
        voto = input('Informe um valor entre 1 e 6: ')

        try:
            if int(voto) in range(1, 7):
                votos_sistema[int(voto) - 1] += 1
            
            elif voto == '0':
                break

            else: #Caso o sistema não esteja na lista disponível
                print(f'O SO número {voto} não foi identificado, tente novamente.')

        except ValueError:
            print(f'O SO número {voto} não foi identificado, tente novamente.')

    
        
    print(votos_sistema)

    total_de_votos = sum(votos_sistema)
    print(total_de_votos)

    for sistema in votos_sistema:
        print(f'O percentual de votos do sistema foi {((sistema/ total_de_votos) * 100):.1f}% dos votos totais')
    
    print(f'Total de votos {total_de_votos}')
    








    pass

best_OS()



