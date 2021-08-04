# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%


salario = float(input('Digite o seu salário: '))
print(f'O seu salário atual é: R${salario}')

if salario > 1250:
    print(f'Você obteve um aumento de 10% \nNovo salário: {salario+(salario*0.1):.2f}')
else:
    print(f'Você obteve um aumento de 15% \nNovo salário: {salario+(salario*0.15):.2f}')