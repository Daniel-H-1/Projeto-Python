print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Escreva um programa qu leia um número n inteiro qualquer, e
mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Quantos termos você desja mostra: '))
t1 = 0
t2 = 1
print('-' * 30)
print('{} -> {}'.format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print(' ')
print('>>>>> FIM <<<<<')
