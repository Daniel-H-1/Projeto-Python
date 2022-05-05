print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('Legenda: VERMELHO = não é divisível pelo número / AZUL = é divisível pelo número')
número = int(input('Digite um número: '))
count = 0
for c in range(1,  número + 1):
    if número % c == 0:
        print('\033[34m', end="")
        count += 1
    else:
        print('\033[31m', end="")
    print('{} '.format(c), end="")

print('\033[m ')
print('O número {} foi divisível por {} números'.format(número, count))
if count == 2:
    print('O número só foi divisível por 1 e {}, Por isso ele é PRIMO!!'.format(número))
else:
    print('O número foi divisível por mais de 2 números, Por isso ele não é PRIMO.')
print('>>>>> FIM <<<<<')
