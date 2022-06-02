print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print(''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e
também indique o menor e o maior valor que estão na tupla.''')

print('=' * 40)
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('GERAÇÃO DE NÚMEROS ALEATÓRIOS NAS TUPLAS')
print('-' * 40)
from random import randint
Valores = (randint(0, 10), randint(0, 250), randint(0, 150), randint(50, 89), randint(0, 150))
print(f'Os valores gerados foram: {Valores}')
print(f'Maior Número: {max(Valores)}')
print(f'Menor Número: {min(Valores)}')
print('-' * 40)
print(f'{"FIM":^40}')

