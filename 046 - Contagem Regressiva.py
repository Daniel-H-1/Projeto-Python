print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Faça um programa que mostre na tela uma Contagem  Regressiva para
o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1  segundo entre eles.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from time import sleep
print('Vamos começar a contagem Regressiva!!!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('>>>>> FIM <<<<<<')
