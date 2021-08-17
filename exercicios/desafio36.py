# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
# será negado.


casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
anos = int(input('Informe por quantos anos pretende pagar: '))
prestacao = casa / (anos*12) # para achar o mes e assim dividir a casa pelo mês

if prestacao > (salario * 0.3):
    print('Empréstimo NEGADO')
else:
    print('Seu empréstimo foi APROVADO')