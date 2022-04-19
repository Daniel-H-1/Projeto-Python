print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Elabore um programa que calcule o valor a sser pago por um produto,'
      'considerando o seu preço normal e condição de pagamento:\n'
      '- À vista dinheiro/cheque: 10% de desconto.\n'
      '- À vista no cartão: 5% de desconto.\n'
      '- Em até 2x no cartão: Preço normal.\n'
      '- 3x no cartão  ou mais: 20% de juros.')

print(' ')
print('{:=^40}'.format(' RESOLUÇÃO DO PROGRAMA '))
print('\nEsse programa calcula o valor do produto de acordo com a forma do pagamento.')
Produto = float(input('Digite o valor do seu produto (Exemplo: 194.99): R$ '))
Pagamento = int(input('''Digite a forma de pagament
[1] Dinheiro/Cheque.
[2] á vista Cartão.
[3] 2x no Cartão.
[4] 3x ou mais.
Digite a sua escolha: '''))

if Pagamento == 1:
      print('O valor do seu produto terá 10% de desconto, logo o valor final do produto é:')
      print(Produto - (Produto * 0.10))
elif Pagamento == 2:
      print('O valor do seu produto terá 5% de desconto, logo o valor final do produto é:')
      print(Produto - (Produto * 0.05))
elif Pagamento == 3:
      print('O valor do seu parcelamento é {}, o pagamento total é {}'.format(Produto / 2, Produto))
elif Pagamento == 4:
      Vezes = int(input('Em quantas parcelas você irá dividir o pagamento?: '))
      Total = Produto + (Produto * 0.20)
      print('O valor do seu produto terá 20% de JUROS, logo será {} parcelas no valor de R$ {:.2f} com JUROS'.format( Vezes , Total / Vezes))
      print('logo o valor final do produto é {}'.format(Total))
else:
      print('O valor digitado não corresponde a nenhuma das opções, \n'
            'então não será possível realizar o calculo!!!')

print('>>>>> FIM <<<<<')

