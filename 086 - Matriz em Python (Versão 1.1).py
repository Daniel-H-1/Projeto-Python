print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('MATRIZ EM PYTHON')
print('-' * 40)
Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        Matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{Matriz[linha][coluna]:^5}]', end="")
    print()
print(f'{"FIM":=^40}')
