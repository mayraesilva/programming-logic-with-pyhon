# Crie um dicionário com os nomes como chaves e as idades como valores. Faça:
# A média das idades.
# Quem é a pessoa mais velha?
# Liste os nomes em ordem decrescente de idade.

nomes_e_idades = {'Maria' : 93, 'Mayra' : 23, 'Karla' : 48 }

def dados_idade(dict_nomes_e_idades):
    #Media das idades
    media = sum(dict_nomes_e_idades.values()) / len(dict_nomes_e_idades.values())
    print(f'Média de idades: {media:.2f} anos')

    #Mais velha:
    mais_velho = 0
    pessoa_mais_velha = 'Ana'

    for pessoa in dict_nomes_e_idades:
        if dict_nomes_e_idades[pessoa] > mais_velho:
            mais_velho = dict_nomes_e_idades[pessoa]
            pessoa_mais_velha = pessoa
    
    print(f'Nome da pessoa mais velha: {pessoa_mais_velha} \n Idade da pessoa mais velha: {mais_velho} anos')
    
    ordem_Decrescente = dict(sorted(dict_nomes_e_idades.items(), key=lambda item: item[1], reverse=True))
    print(f'Em ordem decrescente temos: {ordem_Decrescente}')
    return





dados_idade(nomes_e_idades)