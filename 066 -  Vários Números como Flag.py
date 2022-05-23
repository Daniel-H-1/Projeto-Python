print('''Crie um  programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (Desconsiderando o Flag)''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
n = s = cont = 0
while True:
       s += n
       n = int(input('Digite um valor (Digite 999 para encerrar): '))
       if n == 999:
           break
       cont += 1
print(f"Foram digitados {cont} Números até digitar 999.")
print(f'A soma dos valores digitados é {s}')