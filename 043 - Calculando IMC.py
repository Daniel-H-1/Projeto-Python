print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC \n'
      'e mostre seu status, de acordo com a tabela abaixo:\n'
      '- Abaixo de 18.5: Abaixo do Peso.\n'
      '- Entre 18.5 e 25: Peso Ideal\n'
      '- 25 até 30: Sobrepeso\n'
      '- 30 até 40: Obesidade\n'
      '- Acima de 40: Obesidadde Mórbida')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
print('\nOlá, esse programa calcula seu IMC (Índice de Massa Corporal), então por favor preencha as informações a seguir:')
Peso = float(input('Digite o seu peso (Exemplo: 69.8): '))
Altura = float(input('Digite a sua altura (Exemplo: 1.74): '))
IMC = Peso / (Altura * Altura)

if IMC < 18.5:
      print('Seu IMC é {:.2f}, logo está Abaixo do Peso'.format(IMC))
elif IMC < 25:
      print('Seu IMC é {:.2f}, e está ideal!'.format(IMC))
elif IMC < 30:
      print('Seu IMC é {:.2f}, está com sobrepeso'.format(IMC))
elif IMC <40:
      print('Seu IMC é {:.2f}, está com obesidade'.format(IMC))
elif IMC >40:
      print('Seu IMC é {:.2f}, está com obesidade Mórbida'.format(IMC))
print('>>>>> FIM <<<<<')
