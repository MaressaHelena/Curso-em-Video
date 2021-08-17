# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: mirim
# - Até 14 anos: infantil
# - Até 19 anos: junior
# - Até 20 anos: senior
# - Acima: master

from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria: JUNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')