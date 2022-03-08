import math
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo \n'
      'e calcule a hipotenusa')
print(' ')

cateto_oposto = int(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('De acordo com o cateto oposto e o cateto adjacente, a hipotenusa é {:.1f} '.format(hipotenusa))