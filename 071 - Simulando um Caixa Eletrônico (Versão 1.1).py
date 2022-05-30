print('''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor seráo entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('-' * 40)
print('{:^40}' .format(' CAIXA ELETRÔNICO'))
print('-' * 40)
saque = int(input('Digite o valor do Saque: R$'))
total = saque
cédula = 50
total_cédulas = 0
while True:
    if total >= cédula:
        total -= cédula
        total_cédulas += 1
    else:
        if total_cédulas > 0:
            print(f'O Total de cédulas de R${cédula} é igual {total_cédulas}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédulas = 0
        if total == 0:
            break
print('-' * 40)
print(f'{"FIM":^40}')
