print('''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('TABUADA')
resposta = "S"
count = 1
while resposta not in "Nn":
    print('-' * 30)
    n = int(input('Digite um número para ver a tabuada: '))
    if n < 0:
        print('Programa Encerrado pois o valor digitado é INVÁLIDO!!!')
        break
    while count < 11:
        print(f'{n} x {count} = {n * count}')
        count += 1
    count = 1
    resposta = str(input('Deseja ver a tabuada de outro número [S/N]: '))[0]
print('>>>>> FIM <<<<<')



