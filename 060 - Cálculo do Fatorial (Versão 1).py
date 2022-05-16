print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
n = int(input('Digite o valor de n fatorial: '))
produto = n
count = n-1

while count > 1:
    produto = produto * count
    count = count - 1
print('o valor de {} fatorial é {}'.format(n, produto))
print('>>>>> FIM <<<<<')


