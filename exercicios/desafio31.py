# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
# e R$0,45 para viagens mais longas.


distancia = float(input('Qual é a distância da sua viagem?: '))
viagem_curta = distancia*0.5
viagem_longa = distancia*0.45

if distancia <= 200:
    print(f'Valor da passagem: {viagem_curta}')
else:
    print(f'Valor da passagem: {viagem_longa}')