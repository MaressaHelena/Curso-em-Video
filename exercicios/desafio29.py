# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por km acima do limite.


velocidade = float(input('Qual a velocidade do carro?: '))
multa = (velocidade - 80)*7

if velocidade > 80:
    print(f'🚓 Você foi multado! 🚓 \nO valor cobrado é R$7,00 por cada km acima do limite de 80Km/h. \nValor da multa: R${multa}')
else:
    print('🟢 Dirija com cuidado! 🟢')