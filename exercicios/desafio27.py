# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza


nome = str(input('Digite seu nome: ')).title().strip()
primeiro_nome = nome.split()
primeiro_nome = primeiro_nome[0]
ultimo_nome = nome.split()
ultimo_nome = ultimo_nome[len(ultimo_nome)-1] #comprimento da lista -1 pois a lista começa com 0
print(f'Seu primeiro nome é: {primeiro_nome}')
print(f'Seu último nome é: {ultimo_nome}')