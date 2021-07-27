# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random


nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
sorteio_nome = random.choice[nome1, nome2, nome3, nome4]
sorteio_ordem = random.randrange[1, 4]
print(f' {sorteio_nome} é o {sorteio_ordem} a apresentar! ')