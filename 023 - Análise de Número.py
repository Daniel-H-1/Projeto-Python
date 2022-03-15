print('             >>>>>> INSTRUÇÕES DO PROGRAMA <<<<<<   ')
print('''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS:

Exemplo:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1''')

print(' ')
print('            >>>>>> RESOLUÇÃO DO PROGRAMA <<<<<<   ')

número = int(input('Digite um número: '))
unidade = número // 1 % 10
dezena = número // 10 % 10
centena = número // 100 % 10
milhar = número // 1000 % 10

print('Analisando um número!')
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))



