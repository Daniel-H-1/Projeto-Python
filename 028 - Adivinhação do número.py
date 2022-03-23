import random
from time import sleep
print('>>>>> INSTRUÇÃO DO PROGRAMA <<<<<')
print('Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5,')
print('e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador')
print('Então o programa deverá escrever se o usuário acertou ou não')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('Adivinhe o número!!!')
número = random.choice([0, 1, 2, 3, 4, 5])
chute = int(input('Qual foi o número que o computador "pensou"? '))
print('PROCESSANDO...')
sleep(2)
if número == chute:
      print('Parabéns você acertou o número que o computador pensou!!! {}'.format(número))
else:
      print('Infelizmente você não acertou,  o número que o computador pensou foi o {}.'.format(número))
print('---FIM---')