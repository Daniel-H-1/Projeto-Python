print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Faça um programa que leia três números, e mostre o maior e o menor número digitado')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
#Verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))
