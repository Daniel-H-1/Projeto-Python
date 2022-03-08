from math import cos, sin, tan, radians
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente')
print(' ')

angulo = int(input('Digite o ângulo para o calcular o cosseno, seno e a tangente: '))
cos = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print('O valor do cosseno segundo o angulo é {:.2f}'.format(cos))
print('O valor do seno segundo o angulo é {:.2f}'.format(seno))
print('O valor da tangente segundo o angulo é {:.2f}'.format(tangente))
