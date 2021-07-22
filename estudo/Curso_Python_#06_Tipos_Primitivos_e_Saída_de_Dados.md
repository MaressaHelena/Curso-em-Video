# Tipos Primitivos

 Existem basicamente 4 tipos primitivos em python, são eles:

- `int =` números inteiros (7, 4, -2)
- `float =` números reais ou de ponto flutuante (4.5, 7.8, 0.076, 7.0)
- `bool =` valores lógicos ou boleanos (True ou False; ao trabalhar com bool, sempre usar a primeira letra como maiuscula)
- `str =` caracteres ou strings como: 'Olá', '7.5' ; sempre com uso de aspas (optar por aspas simples), ' ' (string vazia)

Podemos formatar o print utilizando o `.format()`
o `.format()` cria uma espécie de mascára e é sempre lido em ordem.
```py
print(f'A soma vale {a variavel desejada}')
```

## Reconhecendo o tipo primitivo com `type()`
Se eu fosse rodar esse código, o que iria imprimir seria **<class 'str'>** isso porque o tipo primitivo de uma _variável_ precisa ser especificado.

```py
n1 = input('Digite um valor: ')
print(type(n1)) 
```

Aqui imprime **<class 'int'>** pois eu determinei o tipo primitivo
```py
n1 = int(input('Digite um valor: '))
print(type(n1))
```

Aqui vai depender do seguinte, boleano só retorna **True** ou **False**, se eu botar um número qualquer, por exemplo, 7, ele vai retornar **True** porque ele vai entender que sim, existe algo armazenado na variável. Se eu botar nada, ele vai retornar **False**
```py
n1 = bool(input('Digite um valor: '))
print(type(n1))
```
***
##  Funções do tipo `.is`
 
- `.isnumeric()`
Caso eu digite 
```py
# se eu digitar "Oi", ele vai retornar False e claro... "Oi" não é númerico.
n = input('Digite algo: ')
print(n.isnumeric()) 
```
Caso eu digite 5: **True**. Afinal, 5 é numérico
```py
n = input('Digite algo: ')
print(n.isnumeric())
``` 
- `.isalpha()`

Caso eu digite "w": retorna **True**
```py
n = input('Digite algo: ')
print(n.isalpha())
```
Caso eu digite: 3a. **False**. O 3 é numérico 
```py
n = input('Digite algo: ')
print(n.isalpha())
```
- `.isalnum()`

Caso eu digite: 3a. Vai retornar **True**, pois '3a' é alfanumérico, (**3** é numérico e **a** é alfa(letra))
```py
n = input('Digite algo: ')
print(n.isalnum())
```
- `.isupper()`

Verifica se a informação que eu inseri foi escrita com letras maiúsculas. Caso sim, o output dará **True**

```py
n = input('Digite algo: ')
print(n.isupper())
```