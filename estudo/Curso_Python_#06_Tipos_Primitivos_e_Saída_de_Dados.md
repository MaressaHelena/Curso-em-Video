```py
# >>> tipos primitivos

# Existem basicamente 4 tipos primitivos em python, são eles:

int = números inteiros # e.g.: 7, 4, -2
float = números reais ou de ponto flutuante # e.g.: 4.5, 7.8, 0.076, 7.0
bool = valores lógicos ou boleanos # True ou False ; ao trabalhar com bool, sempre usar a primeira letra como maiuscula
str = caracteres ou strings # 'Olá', '7.5' ; sempre com uso de aspas (optar por aspas simples), '' (string vazia)
########################################################################################################################


# podemos formatar o print utilizando o format()
print(f'A soma vale {a variavel desejada}') # o format ele cria uma espécie de mascara e é sempre lido em ordem.

# Para eu saber o tipo primitivo de alguma coisa, é preciso usar a função type()

n1 = input('Digite um valor: ')
print(type(n1)) # se eu fosse rodar esse código, o que iria imprimir seria <class 'str'> isso porque o tipo primitivo de uma variavel precisa ser especificado.

n1 = int(input('Digite um valor: '))
print(type(n1)) # aqui imprime <class 'int'> pois eu determinei o tipo primitivo.

n1 = bool(input('Digite um valor: '))
print(type(n1)) # aqui vai depender do seguinte, boleano só retorna True ou False, se eu botar um numero qualquer, por exemplo, 7, ele vai retornar True porque ele vai entender que sim, existe algo armazenado na variavel. Se eu botar nada, ele vai retornar False.

###########################################################################################################################

# >>> função .isnumeric()

# caso eu digite: 
n = input('Digite algo: ')
print(n.isnumeric()) # se eu digitar 'Oi', ele vai retornar False e claro... Oi não é númerico.

n = input('Digite algo: ')
print(n.isnumeric()) # caso eu digite 5: True. Afinal, 5 é numérico

############################################################################################################################

# >>> função .isalpha()

# caso eu digite: 
n = input('Digite algo: ')
print(n.isalpha()) # se eu digitar 'w', sim, é letra.

n = input('Digite algo: ')
print(n.isalpha()) # caso eu digite: 3a. False. O 3 é numerico 

############################################################################################################################
 # >>> função .isalnum()
 
 # caso eu digite:
n = input('Digite algo: ')
print(n.isalnum()) # se eu digitar: 3a. Vai retornar True, pois '3a' é alfa numerico, (3 é numerico e a é alfa(letra))

############################################################################################################################
 # >>> função .isupper()

# caso eu digite:

n = input('Digite algo: ')
print(n.isupper()) # .isupper verifica se a informação que eu inseri foi escrita com letras maiusculas. Caso sim, o output dará True
```