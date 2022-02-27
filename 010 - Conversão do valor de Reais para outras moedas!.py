print('Conversão do valor de Reais para outras moedas (OBS: Realizado em 02/2022)')
print(' ')
real = float(input('Digite o valor de Reais que você possui? R$'))
dolar = real / 5.17
euro = real / 5.66

print('R${:.2f}  é igual á US${:.2f} Dolár(es)'.format(real, dolar))
print('R${:.2f}  é igual á {:.2f} Euro(s)'.format(real, euro))


