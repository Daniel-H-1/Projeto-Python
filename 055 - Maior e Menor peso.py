print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Faça um programa que leia a peso de cinco pessoas. 
No final mostre o maior e o menor peso lidos.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('Digite o peso de cinco (5) pessoas: ')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (exemplo: 12.5): '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
