# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# - À vista dinheiro/cheque = 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão = preço normal
# - 3x ou mais no cartão = 20% de juros


produto = float(input('Entre com o valor do produto: R$'))
pagamento = int(input('===== Informe o tipo de pagamento =====\n1- (À vista dinheiro/cheque)\n2- (À vista no cartão)\n3- (Em até 2x no cartão)\n4- (3x ou mais no cartão): '))

if pagamento == 1:
    p = produto - (produto*0.1)
    print(f'Você terá um desconto de 10%\nValor a ser pago: R${p}')
elif pagamento == 2:
    p = produto - (produto*0.05)
    print(f'Você terá um desconto de 5%\nValor a ser pago: R${p}')
elif pagamento == 3:
    print('Você não terá desconto\nValor a ser pago: R${p}')
elif pagamento == 4:
    p = produto + (produto*0.2)
    print(f'Você terá um juros de 20%\nValor a ser pago: R${p}')
print('Agradecemos a compra!')