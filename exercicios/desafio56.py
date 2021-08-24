# Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos

somaidade = 0
medidaidade = 0
maioridadehomem = 0
nomehomemvelho = ''
totalmulher20 = 0


for pessoa in range(1, 5):
    print(f'----------- {pessoa} ª PESSOA -----------')
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mn': # sexo in 'Mn' vai buscar se a pessoa digitou M ou m
        nomehomemvelho = nome
        maioridadehomem = idade
    if sexo in 'Mn' and idade > maioridadehomem:
        nomehomemvelho = nome
        maioridadehomem = idade
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1

medidaidade = somaidade / 4
print(f'A media do grupo é: {medidaidade} anos')
print(f'Idade do homem mais velho é: {maioridadehomem}\nSeu nome é: {nomehomemvelho}')
print(f'Total de mulheres abaixo de 20 anos: {totalmulher20}')
