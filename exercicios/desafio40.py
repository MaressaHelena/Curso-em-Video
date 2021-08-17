# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0 = reprovado
# - Média entre 5.0 e 6.9 = recuperação
# - Média 7.0 ou superior = aprovado


nota1 = float(input('Digite o valor da nota 1: '))
nota2 = float(input('Digite o valor da nota 2: '))
media = (nota1+nota2)/2

if media < 5:
    print('Você foi REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Parabéns, você foi APROVADO!!')