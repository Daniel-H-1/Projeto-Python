print('Calcular o aluguel do carro!')
print(' ')

Dias_usados = int(input('Quantos dias você usou o carro? '))
Km_rodados = float(input('Quantos Km rodados o carro possui? '))

Preço_diária = (Dias_usados * 60)
Preço_Km = (Km_rodados * 0.15)
valor_aluguel = (Preço_diária + Preço_Km)

print('Com {} Dias usados e {:.1f} Km rodados, o aluguel custará R${:.2f}'.format(Dias_usados, Km_rodados, valor_aluguel))
