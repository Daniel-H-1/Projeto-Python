print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie um programa que tenha uma tupla única com nomes de produtos,
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços,
organizando os dados em forma tabular.''')

print('=' * 40)
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('LISTAGEM DE PREÇO')
print('-' * 40)
#Tentativa de fazer usando str.
'''Listas_de_Preços = (f'{"Borracha":.<30}R$ {"1000.25":>7}',
                     f'{"Lápis":.<30}R$ {"1.25":>7}')
print(Listas_de_Preços)'''

Lista = ('Borracha', 1.25,
         'Lápis', 0.50,
         'Caderno', 10.50,
         'Estojo', 5.80,
         'Mochila', 35.99)

for pos in range(0, len(Lista)):
    if pos % 2 == 0:
        print(f'{Lista[pos]:.<30}', end='')
    else:
        print(f'R${Lista[pos]:>8}')
print('-' * 40)
print(f'{"FIM":^40}')
