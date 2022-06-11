print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie um programa onde o  usuário possa digitar cinco
valores númericos e cadastre-os em uma lista, já na posição correta
 de inserção (sem usar o sort()).
 No fina, mostre a lista ordenada na tela.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('INSERINDO NÚMEROS EM ORDEM')
print('-' * 40)
Lista_de_Números = list()
for n in range(1, 6):
    número = int(input('Digite um valor: '))
    if n == 1:
        Lista_de_Números.append(número)
        print('Primeiro número adicionado.')
    else:
        for pos, v in enumerate(Lista_de_Números):
            if número <= v:
                Lista_de_Números.insert(pos, número)
                print(f'Adicionando o número.')
                break
            elif número > max(Lista_de_Números):
                Lista_de_Números.append(número)
                print(f'Adicionando no Final da Lista.')
                break
print('-' * 40)
print(f'Observe a lista a seguir: {Lista_de_Números}')
print(f'{"FIM":=^40}')

