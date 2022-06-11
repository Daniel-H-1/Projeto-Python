print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie um programa onde o  usuário possa digitar cinco
valores númericos e cadastre-os em uma lista, já na posição correta
 de inserção (sem usar o sort()).
 No fina, mostre a lista ordenada na tela.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('INSERINDO NÚMEROS NA ORDEM')
print('-' * 40)
Lista = []
for c in range(0,  5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > Lista[-1]:
        Lista.append(n)
        print('Adicionando ao Final da Lista.')
    else:
        pos = 0
        while pos < len(Lista):
            if n <= Lista[pos]:
                Lista.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print('-' * 40)
print(f'{"FIM":=^40}')
