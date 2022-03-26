print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Identifique se o número é par ou ímpar.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
número = int(input('Digite um número: '))
par = número / 1 % 10
if par == 0:
    print('O número {} apresentado é par!'.format(número))
else:
    print('O número {} apresentado é ímpar!'.format(número))
print('---FIM---')
