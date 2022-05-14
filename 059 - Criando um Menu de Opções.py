print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multipllicar
[3] Maior número
[4] Novos números
[5] O computador gerará números novos
[6] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from random import randint

print('CRIANDO UM MENU DE OPÇÕES!!!')
opção = 0
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

while opção != 6:
    print("=-" * 10)
    print('O QUE VOCÊ DESEJA FAZER COM ESSES VALORES?')
    print('[1] Somar [2] Multiplicar [3] Maior Número [4] Novos números [5] Computador Gerará Novo Números [6] Nada, Quero sair do Programa')
    opção = int(input('Digite a sua opção: '))
    if opção == 1:
        print('A soma dos valores é {}'.format(valor1 + valor2))
    elif opção == 2:
        print('O resultado da multiplicação é {}'.format(valor1 * valor2))
    elif opção == 3:
        if valor1 > valor2:
            print('O maior número é {}'.format(valor1))
        elif valor2 > valor1:
            print('O maior número é {}'.format(valor2))
        else:
            print('Os valores são iguais!!!')
    elif opção == 4:
        print('Digite os novos Números!')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        valor1 = randint(1, 50)
        valor2 = randint(1, 50)
        print('Os novos números são {} e {}'.format(valor1, valor2))
    elif opção != 6:
        print('Opção Inválida!!!')
print('>>>>> FIM <<<<<')
