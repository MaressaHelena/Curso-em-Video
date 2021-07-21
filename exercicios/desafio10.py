# O exercicio corresponde a aula 7 do CURSO EM VÍDEO.


# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere o dólar do dia, por exemplo: US$1.00 = R$ 3.27

carteira = float(input('Insira sua quantia de dinheiro: '))
compra_dolar = carteira/5.19
print(f'Você tem R${carteira} ! Você pode comprar U${round(compra_dolar, 2)}')
print('FIM')
