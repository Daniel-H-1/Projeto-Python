print('''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor seráo entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
while True:
    print('-' * 40)
    print('{:^40}' .format(' CAIXA ELETRÔNICO'))
    print('-' * 40)
    saque = int(input('Digite o valor do Saque: R$'))
    total = saque
    total_cédulas = cédulas_50 = cédulas_20 = cédulas_10 = cédulas_1 = 0
    while total >= 50:
        total -= 50
        cédulas_50 += 1
        total_cédulas +=1
    while total >= 20:
        total -= 20
        cédulas_20 += 1
        total_cédulas += 1
    while total >= 10:
        total -= 10
        cédulas_10 += 1
        total_cédulas += 1
    while total >= 1:
        total -= 1
        cédulas_1 += 1
        total_cédulas += 1
    print(f"Foram retiradas {cédulas_50} Cédulas de R$50.")
    print(f"Foram retiradas {cédulas_20} cédulas de R$20.")
    print(f"Foram retiradas {cédulas_10} cédulas de R$10.")
    print(f"Foram retiradas {cédulas_1} cédulas de R$1.")
    resposta = str(input('Você deseja realizar outro saque? [S/N]: ')).strip().upper()[0]
    while resposta not in "Nn":
        resposta = str(input('Você deseja realizar outro saque? [S/N]: ')).strip().upper()[0]
    if resposta == 'N' or 'n':
        break
print('-' * 40)
print(f'{"FIM":^40}')
