print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Faça um programa que calcule a soma entre todos os números ímpares 
que são múltiplos de três e que se encontram no intervalo de 1 até 500.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
s = 0
cont = 0
print('Os número impares  em múltiplos de 3 entre 1 até 500 são: ')
for c in range(1, 501, 2):
    n = c
    if (n % 3) == 0:
        print(c, end=" ")
        cont = cont + 1
        s += n
print(' ')
print('Os números somados forma {} números que atingiram os requisitos,'.format(cont))
print('e a soma dos valores ímpares múltiplos de 3 é {}'.format(s))
print('>>>>> FIM <<<<<')
