print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
s = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if (n % 2) == 0:
        s += n
        count += 1
print('Você digitou {} números pares e '.format(count), end="")
print('a soma dos valores PARES digitados é {}.'.format(s))
