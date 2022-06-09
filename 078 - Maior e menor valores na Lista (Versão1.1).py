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
maior = menor = 0
for n in range(0, 5):
    Valores.append(int(input(f'Digite o valor para a posição {n}: ')))
    if n == 0:
        maior = menor = Valores[n]
    else:
        if Valores[n] < menor:
            menor = Valores[n]
        if Valores[n] > maior:
            maior = Valores[n]
print(f'Observe os Valores da Lista: {Valores}')
print(f'O Maior valor da Lista é {maior} na posição:', end=" ")
for i, v in enumerate(Valores):
    if v == maior:
        print(f'{i}...', end="")
print()
print(f'O Menor valor da Lista é {menor} na posição:', end=" ")
for pos, v in enumerate(Valores):
    if v == menor:
        print(f'{pos}...', end="")
print()
print(f'{"FIM":=^40}')
