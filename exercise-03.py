# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são: 
# "Telefonou para a vítima?" 
# "Esteve no local do crime?"
#  "Mora perto da vítima?"
#  "Devia para a vítima?"
#  "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#  entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

questions = [input('Telefonou para a vítima? '), 
            input('Esteve no local do crime? '), 
            input('Mora perto da vítima? '), 
            input('Devia para a vítima? '), 
            input('Já trabalhou com a vítima? ')]



def crime_part(answers):
    #quantidades de sim
    # inocente <= 1
    # suspeita = 2 #sim
    # cumplice =  [3, 4]
    # assassino = 5
    

    inocencia_questionada = []

    for answer in answers:
        if answer == 's':
            inocencia_questionada.append(inocencia_questionada)
    
    if len(inocencia_questionada) <= 1:
        return 'A pessoa avaliada é inocente'
    
    elif len(inocencia_questionada) == 2:
        return 'A pessoa avaliada é suspeita'
    
    elif len(inocencia_questionada) >= 3 and len(inocencia_questionada) <= 4:
        return 'A pessoa avaliada é cúmplice'
    
    elif len(inocencia_questionada) == 5:
        return 'A pessoa avaliada é o assassino, prenda-a'


print(crime_part(questions))


