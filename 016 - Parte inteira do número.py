from math import floor
print('Crie um programa que leia um número Real, e mostre a parte inteira do número na tela')

numeroInteiro = float(input('Digite um número como esse (5.326) e descubra a sua parte inteira: '))

print('A parte inteira de {}, é igual á {}'.format(numeroInteiro, floor(numeroInteiro)))