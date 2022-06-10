print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie um programa onde o usuário possa digitar vários valores
númericos e cadestre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('INSERINDO DIVERSO NÚMEROS')
print('-' * 40)
Números = list()
while True:
    n = int(input('Digite um número inteiro: '))
    if Números.count(n) == 0:
        Números.append(n)
    else:
        print('O número não será adicionado, pois ele já existe na lista!!!')
    resposta = str(input('Quer digitar outro número [S/N]: ')).strip()[0]
    while resposta not in 'NnSs':
        print('Resposta INVÁLIDA!!!')
        resposta = str(input('Quer digitar outro número [S/N]: '))
    if resposta in 'Nn':
        break
Números.sort()
print(f'Os números digitados em ordem crescente são: {Números}')
print('-' * 40)
print(f'{"FIM":=^40}')
