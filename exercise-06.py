# As Organizações Tabajara resolveram dar um abono aos seus colaboradores
#  em reconhecimento ao bom resultado alcançado durante o ano que passou. 
# Para isto contratou você para desenvolver a aplicação que servirá como
#  uma projeção de quanto será gasto com o pagamento deste abono. 
# Após reuniões envolvendo a diretoria executiva,
#  a diretoria financeira e os representantes do sindicato laboral, 
# chegou-se a seguinte forma de cálculo:



# Cada funcionário receberá o equivalente a 20% do seu salário bruto de
# dezembro;
# O piso do abono será de 100 reais, isto é, aqueles funcionários cujo
# salário for muito baixo recebem este valor mínimo;
# Neste momento, não se deve ter nenhuma preocupação com colaboradores com
# tempo menor de casa, descontos, impostos ou outras particularidades.


# Seu programa deverá permitir a digitação do salário de um número indefinido
#  (desconhecido) de salários. 
# Um valor de salário igual a 0 (zero) encerra a digitação. 
# Após a entrada de todos os dados o programa deverá 
# calcular o valor do abono concedido a cada colaborador, 
# de acordo com a regra definida acima. Ao final, o programa deverá apresentar: 
# O salário de cada funcionário, juntamente com o valor do abono; 
# O número total de funcionários processados; 
# O valor total a ser gasto com o pagamento do abono; 
# O número de funcionários que receberão o valor mínimo de 100 reais; 
# O maior valor pago como abono;

# Exemplo: Projeção de Gastos com Abono
# Salário: 1000 Salário: 300 Salário: 500 Salário: 100 Salário: 4500 Salário: 0

# Salário - Abono 
# R$ 1000.00 - R$ 200.00 
# R$ 300.00 - R$ 100.00
# R$ 500.00 - R$ 100.00 
# R$ 100.00 -  R$ 100.00 
# R$ 4500.00 - R$ 900.00

# Foram processados 5 colaboradores 
# Total gasto com abonos: R$ 1400.00
#  Valor mínimo foi pago a 3 colaboradores 
# Maior valor de abono pago: R$ 900.00

def abono_salarial():

    salario = 0
    salarios = []
    bonus_salarial = []
    valor_minimo_count = 0
    total_de_colaboradores = len(salarios)

    while salario != '0':
        salario = input('Informe seu salário em reais: ')

        try:

            if salario == '0':
                break

            else:
                salarios.append(int(salario))
            
            
        except ValueError:
            print(f'O salário {salario} não foi lido corretamente, tente novamente.')

    print(salarios)


    for salario in salarios:
        bonus = salario * 0.2

        if bonus < 100:
            bonus = 100
            valor_minimo_count += 1
            bonus_salarial.append(bonus)
            
        
        else:
            bonus_salarial.append(bonus)

    maior_bonus = max(bonus_salarial)
    total_gasto_abono = sum(bonus_salarial)



    for salario, bonus in zip(salarios, bonus_salarial):
        print(f'O colaborador com salario de R$ {salario},00 recebeu o abono de R$ {bonus},00')

    print(f'Foram processados {total_de_colaboradores} colaboradores')
    print(f'Total gasto com abonos: R$ {total_gasto_abono},00')
    print(f'O valor mínimo foi pago a {valor_minimo_count} colaboradores')
    print(f'O maior valor de abono pago: R$ {maior_bonus},00')
            

    return bonus_salarial

abono_salarial()