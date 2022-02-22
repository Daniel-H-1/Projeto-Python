print('Convertendo um valor de Metros para centímetros ou milímetros!')


medida = float(input('Digite um valor em metros: '))

dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10


print('{} metros é igual a {:.0f} centímetros e {:.0f} milímetros'.format(medida, cm, mm))
print('é igual a {}dm'.format(dm))
print('é igual a {}km'.format(km))
print('é igual a {}hm'.format(hm))
print('é igual a {}dam'.format(dam))
