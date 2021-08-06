# Cores no Terminal

Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os programas em Python. Para isso, devemos sempre utilizar o comando `\033[style;text;backgroundm)`

### Style

- 0
   Sem estilo
- 1
   Bold = negrito
- 4
   Underline = sublinhado
- 7
   Negative = irá inverter as configurações

### Text

- 30
   black
- 31
   red
- 32
   green
- 33
   yellow
- 34
   blue
- 35
   magenta
- 36
   cyan
- 37
   grey
- 97
   white

### Background

- 40
   black
- 41
   red
- 42
   green
- 43
   yellow
- 44
   blue
- 45
   magenta
- 46
   cyan
- 47
   grey
- 107
   white
***
### Exemplos

1.
```py
print('\033[4;31;46mOlá, Mundo!')
```
2.
```py
print('\033[1;31;43mOlá, Mundo!\033[m') # esse exemplo se difere do 1. pois dessa forma, a cor fica somente no alcance das letras
```
3.
```py
print('\033[7;31;43mOlá, Mundo!\033[m') #inversão
```
4.
```py
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}') # para finalizar o alcance de uma cor basta colocar o código no começo e onde desejar que seja o fim
```
