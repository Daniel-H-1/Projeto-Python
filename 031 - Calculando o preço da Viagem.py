print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Desenvolva um programa que pergunte a distância de uma viagem em Km.')
print('Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')

Distância = int(input('Digite a distância da sua viagem em Km: '))
if Distância <= 199:
    print('O preço da passagem será R${}'.format(Distância * 0.50))
else:
    print('O preço da passagem será R${}'.format(Distância * 0.45))
print('---FIM---')

'''Distância = float(input('Digite a distância da sua viagem em km: '))
preço = Distância * 0.50 if Distância <= 200 else Distância * 0.45
print('O preço da sua passagem será R${}'.format(preço))
'''#Código com uma condição simplificada
