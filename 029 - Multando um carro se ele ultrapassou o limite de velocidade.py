print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Escreva um programa que leia a velocidade de um carro,')
print('Se ele ultrapassar 80 Km, escreva que ele foi multado, e para cada Km excedido é 7,00 Reais a multa')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
Km = int(input('Digite a velocidade do carro em km: '))
if Km > 80:
    multa = (Km - 80) * 7
    print('Pela velocidade excessiva seu carro foi multado no valor de R${}'.format(multa))
else:
    print('De acordo com sua velocidade o seu carro não foi multado.')