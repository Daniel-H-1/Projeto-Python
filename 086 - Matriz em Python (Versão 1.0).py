print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('MATRIZ EM PYTHON')
print('-' * 40)
Matriz = [[], [], []]
count = linha =  0
for números in range(1, 10):
    n = int(input(f'Digite um valor para [{linha}, {count}]: '))
    count += 1
    if números == 3 or números == 6:
        linha += 1
        count = 0
    if números <= 3:
        Matriz[0].append(n)
    elif números <= 6:
        Matriz[1].append(n)
    elif números <= 9:
        Matriz[2].append(n)
print('-' * 40)
for v in Matriz:
    print(v)
print(f'{"FIM":=^40}')
