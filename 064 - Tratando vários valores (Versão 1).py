print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag 999)>''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
n = soma = count = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        soma += n
        count += 1
print('Você digitou {} números até digitar o 999'.format(count))
print('A soma dos valores digitados {}'.format(soma))
