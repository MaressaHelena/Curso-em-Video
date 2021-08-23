# Estrutura de Repetição: For

### Laço de repetição ou iteração

Também é conhecido como laço com variável de controle

```py
for c in range(0,11): #será uma contagem de 0 à 11 ignorando o 11, ficando então de 0 à 10
    print(c)
print('fim')
```
##### obs: `c` representa a variável de controle

- Exemplos:
    - ```py
        for c in range(0, 6):
            print(c)
        print('FIM')
        ```
    - ```py
        for c in range(6, 0, -1) #contagem regressiva
            print(c)
        print('FIM')
        ```
    - ```py
        for c in range(0, 7, 2):
            print(c)
        print('FIM')
        ```
    - ```py
        n = int(input('Digite um número')) # irá desconsiderar o último número
        for c in range(0, n):
            print(c)
        print('FIM')
        ```
    - ```py
        n = int(input('Digite um número')) # terá exatamente o valor desejado
        for c in range(0, n+1):
            print(c)
        print('FIM')
        ```
    - ```py
        i = int(input('INICIO: '))
        f = int(input('FIM: '))
        p = int(input('PASSO: '))
        for c in range(i, f+1, p):
            print(c)
        print('FIM')
        ```
    - ```py
        for c in range(0, 3):
            n = int(input('Digite um valor: '))
        print('FIM')
        ```
    - ```py
        s = 0
        for c in range(0, 4):
            n = int(input('Digite um valor'))
            s += n
        print(f'O SOMATÓRIO DE TODOS OS VALORES É: {s}')
        ```