print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Aprimore o desafio anterior, mostrando no final: 

A) A soma de todas os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('MATRIZ EM PYTHON')
print('-' * 40)
Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaColuna3 = 0
#recebendo os dados na Lista.
for linha in range(0, 3):
    for coluna in range(0, 3):
        Matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
#Escrevendo os dados na tela (PRINT)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{Matriz[linha][coluna]:^5}]', end="")
    print()
#Analisando os valores e somando.
for linha in range(0, 3):
    for coluna in range(0, 3):
        #Somando os Pares
        if Matriz[linha][coluna] % 2 == 0:
            somaPares += Matriz[linha][coluna]
#Somando a coluna 3 da Matriz
for linha in range(0, 3):
    somaColuna3 += Matriz[linha][2]
#Maior valor da linha 2
for coluna in range(0, 3):
    if coluna == 0:
        maior = Matriz[1][coluna]
    elif Matriz[1][coluna] > maior:
        maior = Matriz[1][coluna]
print('-' * 40)
print(f'Soma dos Pares é {somaPares}')
print(f'A soma da terceira coluna é {somaColuna3}')
print(f'O maior valor da segunda linha é {maior}')
print(f'{"FIM":=^40}')