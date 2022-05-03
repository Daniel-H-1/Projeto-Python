print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
termo = int(input('Digite o primeiro termo da progressão: '))
Razão = int(input('Digite a razão da PA: '))
n = 1
for c in range(termo, 10):
    print('{}º Termo: {}'.format(n, termo))
    termo += Razão
    n += 1
print('>>>>> FIM <<<<<')
