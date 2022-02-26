print('11 - Leia a altura de uma parede em metros, calcule sua área e \n'
      'a quantidade necessária par pinta-la sabendo que cada litro de tinta pinta uma área de 2m² \n')

n1 = float(input('Digite a Altura da sua parede: '))
n2 = float(input('Digite a Largura da parede: '))
a = n1 * n2

print('A área da parede é {}, sendo assim será necessário {} litros de tinta, \n'
      'considerando que cada litro de tinta pinta 2m².'.format(a, a/2))