# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"


cidade = str(input('Digite o nome da sua cidade: ')).strip()
inicial = cidade.capitalize().split()
santo = 'Santo' in inicial[0]
print(santo)