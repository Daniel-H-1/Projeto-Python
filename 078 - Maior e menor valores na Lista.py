print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Faça um programa que leia 5 valores, e guarde-os em uma lista.
No final mostre qual foi o maior e o menor valores digitados
e as suas respectivas posições na lista.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('Digite 5 valores a seguir para a Lista!!!!')
Valores = []
for n in range(1, 6):
    Valores.append(int(input(f'Digite o {n}º valor: ')))
print(f'Observe os Valores da Lista: {Valores}')
print(f'O Maior valor da Lista é {max(Valores)}.')
print(f'O Menor valor da Lista é {min(Valores)}.')
print(f'{"FIM":=^40}')

