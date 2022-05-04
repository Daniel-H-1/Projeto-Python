print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('')
primeiro = int(input('Digite o primeiro termo da progressão: '))
Razão = int(input('Digite a razão da PA: '))
décimo = primeiro + (10 - 1) * Razão
for c in range(primeiro, décimo + Razão, Razão):
    print('{}'.format(c), end=" > ")
print(' ')
print('>>>>> FIM <<<<<')