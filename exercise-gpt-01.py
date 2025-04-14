#Crie uma lista com 10 nomes de pessoas. Depois:
#Imprima apenas os nomes que começam com a letra "A".
#Crie uma nova lista com o tamanho de cada nome.

nomes = ['Ana', 'Amelia', 'Bruna', 'Bianca', 'Caio', 'Mayra', 
         'Angelina', 'Camilly', 'Mariana', 'Daniel']

tamanho_nomes = []


for nome in nomes:
    for letra in nome:
        if letra == 'A':
            print(nome)
    
    tamanho = len(nome)
    tamanho_nomes.append(tamanho)


for nome, tamanho in zip(nomes, tamanho_nomes):
    print(f'O  nome {nome} tem {tamanho} letras')
    
