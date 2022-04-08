print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.\n'
      'O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.\n'
      'Condição: Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então '
      'o empréstimo será negado.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('Olá, sou o assistente virual e estou aqui para verificar a possibbilidade do empréstimo, \n'
      'então por favor preencha as seguintes informações:')
Casa = float(input('Digite o valor da casa: R$ '))
Salário = float(input('Digite o seu salário: R$ '))
Meses = int(input('Em quantos meses você pretende pagar?: '))
Prestação = Casa / Meses

print(' ')
if Prestação <= (Salário * 0.30):
      print('A prestação da casa de R$ {:.2f} dividida por {} meses é R$ {:.2f}'.format(Casa, Meses, Prestação), end='')
      print(' Logo o empréstimmo foi aprovado!!')
else:
      print('O empréstimo foi negado pois as prestações custarão um valor maior que 30% de seu salário!')
print('Qualquer outra dúvida se comunique com o seu banco!!!!')
