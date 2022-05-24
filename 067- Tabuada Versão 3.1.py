print('''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.''')

print(' ')

print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for t in range(1, 11):
        print(f'{n} x {t} = {n*c}')
    print('-' * 30)
print('O programa Acabou!!!')
print('>>>>> FIM <<<<<')
