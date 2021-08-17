# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo


idade = int(input('Informe sua idade: '))
print(f'Ano de nascimento: {2021-idade}')

if idade < 18:
    falta = 18 - idade
    print('Você ainda se alistará ao serviço militar!')
    print(f'Faltam {falta} ano(s) ainda!')
elif idade == 18:
    print('Já está na hora de se alistar ao serviço militar!')
elif idade > 18:
    atraso = idade - 18
    print('Você passou do tempo de alistamento!')
    print(f'Seu atraso é de {atraso} ano(s)')
print('Tenha um ótimo dia')